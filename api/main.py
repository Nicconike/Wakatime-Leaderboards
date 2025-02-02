"""Main Runner Script to fetch the latest stats & generate the Wakatime Leaderboards"""

import base64
import math
import os
import logging
import time
from typing import Dict, Optional
import requests
from github import GithubException
from api.utils import initialize_github, commit_to_github

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Required Secrets Configuration
WAKATIME_API_KEY = os.environ["INPUT_WAKATIME_API_KEY"]
REQUEST_TIMEOUT = (25, 30)
README = "README.md"

# Version Identifier for Changelog
__version__ = "1.2.1"


def format_time(seconds):
    """Format Time to readable format"""
    hours, remainder = divmod(seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    if hours == 0:
        if minutes == 1:
            return "1 min"
        return str(int(minutes)) + " mins"
    if minutes == 0:
        return str(int(hours)) + " hr" + ("" if hours == 1 else "s")
    return (
        str(int(hours))
        + " hr"
        + ("" if hours == 1 else "s")
        + " "
        + str(int(minutes))
        + " min"
        + ("s" if minutes > 1 else "")
    )


def handle_successful_response(response):
    """Handle successful HTTP response by validating and returning the data"""
    data = response.json().get("data", {})
    if not data.get("is_up_to_date", True):
        logger.warning("Received 200 but stats are not finalized")
        raise ValueError("WakaTime stats still processing")

    if not data or data.get("total_seconds", 0) == 0:
        logger.info("No coding activity detected")
        return None

    logger.debug("Successfully fetched valid stats")
    return data


def handle_retryable_error(response, delay, attempt):
    """Handle retryable HTTP errors by logging and delaying the next attempt"""
    logger.warning(
        "Retryable error %d - Retrying in %ds (attempt %d)",
        response.status_code,
        delay,
        attempt,
    )
    time.sleep(delay)


def handle_client_error(response):
    """Handle client-side HTTP errors by logging and raising a ValueError"""
    error_msg = (
        f"Client error {response.status_code}. " "Validate API key and permissions"
    )
    logger.error(error_msg)
    raise ValueError(error_msg)


def handle_unexpected_status(response):
    """Handle unexpected HTTP status codes by logging and raising a ValueError"""
    error_msg = f"Unexpected HTTP {response.status_code}"
    logger.error(error_msg)
    raise ValueError(error_msg)


def handle_network_error(e, delay):
    """Handle network-related errors by logging and delaying the next attempt"""
    logger.warning("Network error: %s - Retrying in %ds", str(e), delay)
    time.sleep(delay)


def handle_exhausted_retries(max_retries):
    """Handle the scenario where the maximum number of retries is exhausted"""
    final_error = (
        f"Failed after {max_retries} retries. " "WakaTime stats never became available"
    )
    logger.error(final_error)
    raise ValueError(final_error)


def get_wakatime_stats(api_key: str) -> Optional[Dict]:
    """Fetch WakaTime stats with robust retry logic and WakaTime-specific validation"""
    max_retries = 8
    backoff_factor = 2
    max_delay = 200

    url = "https://wakatime.com/api/v1/users/current/stats/last_7_days"
    auth_string = f"Basic {base64.b64encode(api_key.encode()).decode()}"
    headers = {"Authorization": auth_string}

    attempt = 0
    delay = 5

    while attempt < max_retries:
        attempt += 1
        try:
            response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
            logger.debug(
                "Attempt %d/%d: HTTP %d", attempt, max_retries, response.status_code
            )

            if response.status_code == 200:
                return handle_successful_response(response)

            if response.status_code in {202} or 500 <= response.status_code < 600:
                handle_retryable_error(response, delay, attempt)
                delay = min(math.ceil(delay * backoff_factor), max_delay)
                continue

            if 400 <= response.status_code < 500:
                handle_client_error(response)

            handle_unexpected_status(response)

        except (requests.ConnectionError, requests.Timeout) as e:
            handle_network_error(e, delay)
            delay = min(math.ceil(delay * backoff_factor), max_delay)
            continue

    handle_exhausted_retries(max_retries)
    return None


def get_leaderboards(api_key):
    """Get current user's Wakatime leaderboards stats"""
    url = "https://wakatime.com/api/v1/leaders"
    auth_string = "Basic " + base64.b64encode(api_key.encode()).decode()
    headers = {"Authorization": auth_string}

    stats = get_wakatime_stats(api_key)
    if stats is None:
        return {
            "total_coding_time": 0,
            "top_language": None,
            "language_times": {},
            "global": {},
            "language": {},
        }

    languages = stats.get("languages", [])
    top_language = languages[0]["name"] if languages else None
    total_coding_time = stats.get("total_seconds", 0)
    leaderboards = {
        "total_coding_time": total_coding_time,
        "top_language": top_language,
        "language_times": {lang["name"]: lang["total_seconds"] for lang in languages},
    }

    response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
    if response.status_code == 200:
        leaderboards["global"] = response.json().get("current_user", {})

    if top_language:
        language_url = url + "?language=" + top_language
        response = requests.get(language_url, headers=headers, timeout=REQUEST_TIMEOUT)
        if response.status_code == 200:
            leaderboards["language"] = response.json().get("current_user", {})

    return leaderboards


def format_leaderboard_data(leaderboards):
    """Format Leaderboard Stats Data"""
    markdown = "### Wakatime Leaderboards (Worldwide)\n\n"
    total_coding_time = leaderboards["total_coding_time"]
    if total_coding_time == 0:
        return markdown + "No coding activity detected in the past week.\n\n"

    def create_table(title, data, total_seconds):
        table = "#### " + title + "\n\n"
        table += "| Ranked | Hours Coded | Daily Avg |\n"
        table += "| ------ | ----------- | --------- |\n"
        rank = str(data.get("rank", "-"))
        hours = format_time(total_seconds)
        daily_avg = format_time(total_seconds / 7)
        table += "| " + rank + " | " + hours + " | " + daily_avg + " |\n\n"
        return table

    markdown += create_table(
        "Public Leaderboards (Weekly)",
        leaderboards.get("global", {}),
        total_coding_time,
    )

    top_language = leaderboards.get("top_language", "Unknown")
    language_time = leaderboards["language_times"].get(top_language, 0)
    markdown += create_table(
        "Top Language (" + top_language + ")",
        leaderboards.get("language", {}),
        language_time,
    )

    return markdown


def update_readme(repo, markdown_data, start_marker, end_marker):
    """Update the README.md file with the provided Markdown content within specified markers"""
    try:
        readme_file = repo.get_contents(README)
        readme_content = readme_file.decoded_content.decode("utf-8")
        start_index = readme_content.find(start_marker)
        end_index = readme_content.find(end_marker, start_index)

        if start_index == -1 or end_index == -1:
            logger.error("Markers not found: %s", start_marker)
            return None

        new_section_content = start_marker + "\n" + markdown_data + "\n" + end_marker

        if (
            new_section_content
            != readme_content[start_index : end_index + len(end_marker)]
        ):
            return new_section_content

        return None

    except (FileNotFoundError, PermissionError, IOError) as e:
        logger.error("Error occurred while updating README: %s", str(e))
        return None


def get_readme_content(repo):
    """Get the current content of README file"""
    readme_file = repo.get_contents(README)
    if isinstance(readme_file, list):
        readme_file = readme_file[0]
    return readme_file.decoded_content.decode("utf-8")


def update_wakatime_stats():
    """Function to update Wakatime stats in README"""
    if not WAKATIME_API_KEY:
        raise ValueError("WAKATIME_API_KEY environment variable not set")

    repo = initialize_github()
    leaderboards = get_leaderboards(WAKATIME_API_KEY)
    formatted_data = format_leaderboard_data(leaderboards)

    # Handle no coding stats
    if not leaderboards or leaderboards["total_coding_time"] == 0:
        logger.info("No coding activity detected in the past week")
        return

    start_marker = "<!-- Wakatime-Start -->"
    end_marker = "<!-- Wakatime-End -->"
    new_section_content = update_readme(repo, formatted_data, start_marker, end_marker)

    if new_section_content:
        readme_content = get_readme_content(repo)
        if readme_content is None:
            logger.error("Failed to retrieve README content")
            return

        start_index = readme_content.find(start_marker)
        end_index = readme_content.find(end_marker, start_index) + len(end_marker)
        updated_readme_content = (
            readme_content[:start_index]
            + new_section_content
            + readme_content[end_index:]
        )

        files_to_update = {README: updated_readme_content}
        if commit_to_github(repo, files_to_update):
            logger.info("Updated README with Wakatime Leaderboards")
        else:
            logger.error("Failed to commit changes to GitHub")
    else:
        logger.info("No changes needed in README")


def log_execution_time(start_time):
    """Log the total execution time of the script"""
    total_time = round(time.time() - start_time, 3)
    if total_time > 60:
        minutes, seconds = divmod(total_time, 60)
        logger.info(
            "Total Execution Time: %d minutes and %.3f seconds", minutes, seconds
        )
    else:
        logger.info("Total Execution Time: %.3f seconds", total_time)


def main():
    """Main function to run the script"""
    start_time = time.time()

    try:
        update_wakatime_stats()
    except ValueError as ve:
        logger.error("Value Error: %s", str(ve))
    except GithubException as ge:
        logger.error("GitHub Error: %s", str(ge))
    except requests.RequestException as re:
        logger.error("Request Error (possibly WakaTime API issue): %s", str(re))
    except IOError as ioe:
        logger.error("I/O Error: %s", str(ioe))
    except KeyError as ke:
        logger.error("Key Error (possibly missing data in API response): %s", str(ke))

    log_execution_time(start_time)


if __name__ == "__main__":
    main()
