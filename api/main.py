"""Main Runner Script to fetch the Wakatime Stats & Generate Wakatime Leaderboards Stats"""

import base64
import os
import logging
import time
import requests
from github import GithubException
from api.utils import initialize_github, commit_to_github

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Required Secrets Configuration
WAKATIME_API_KEY = os.environ["INPUT_WAKATIME_API_KEY"]

REQUEST_TIMEOUT = (25, 30)

# Version Identifier for Changelog
__version__ = "1.1.0"


def format_time(seconds):
    """Format Time to readable format"""
    hours, remainder = divmod(seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    if hours > 0 or minutes >= 60:
        return str(int(hours)) + " hrs " + str(int(minutes)) + " mins"
    return str(int(minutes)) + " mins"


def get_wakatime_stats(api_key):
    """Get current user's Wakatime stats"""
    url = "https://wakatime.com/api/v1/users/current/stats/last_7_days"
    auth_string = "Basic " + base64.b64encode(api_key.encode()).decode()
    headers = {"Authorization": auth_string}
    response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
    if response.status_code == 200:
        return response.json().get("data", {})
    raise ValueError("Failed to fetch user stats: " + str(response.status_code))


def get_leaderboards(api_key):
    """Get current user's Wakatime leaderboards Stats"""
    url = "https://wakatime.com/api/v1/leaders"
    auth_string = "Basic " + base64.b64encode(api_key.encode()).decode()
    headers = {"Authorization": auth_string}

    stats = get_wakatime_stats(api_key)
    languages = stats.get("languages", [])
    top_language = languages[0]["name"] if languages else None
    total_coding_time = stats.get("total_seconds", 0)

    leaderboards = {
        "total_coding_time": total_coding_time,
        "top_language": top_language,
        "language_times": {lang["name"]: lang["total_seconds"] for lang in languages},
    }

    # Global leaderboard
    response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
    if response.status_code == 200:
        global_data = response.json().get("current_user", {})
        leaderboards["global"] = global_data
        # Extract country from global data
        leaderboards["country_name"] = (
            global_data.get("user", {}).get("city", {}).get("country", "Unknown")
        )

    # Language leaderboard
    if top_language:
        language_url = url + "?language=" + top_language
        response = requests.get(language_url, headers=headers, timeout=REQUEST_TIMEOUT)
        if response.status_code == 200:
            language_data = response.json().get("current_user", {})
            leaderboards["language"] = language_data

    return leaderboards


def format_leaderboard_data(leaderboards):
    """Format Leaderboard Stats Data"""
    markdown = "### Wakatime Leaderboards (Worldwide)\n\n"

    def create_table(title, data, total_seconds):
        table = "#### " + title + "\n\n"
        table += "| Ranked | Hours Coded | Daily Avg |\n"
        table += "| ------ | ----------- | --------- |\n"
        rank = str(data.get("rank", "-"))
        hours = format_time(total_seconds)
        daily_avg = format_time(total_seconds / 7)
        table += "| " + rank + " | " + hours + " | " + daily_avg + " |\n\n"
        return table

    total_coding_time = leaderboards["total_coding_time"]

    # Public Leaderboards (Weekly)
    global_data = leaderboards.get("global", {})
    markdown += create_table(
        "Public Leaderboards (Weekly)", global_data, total_coding_time
    )

    # Top Language
    language_data = leaderboards.get("language", {})
    top_language = leaderboards.get("top_language", "Unknown")
    language_time = leaderboards["language_times"].get(top_language, 0)
    markdown += create_table(
        "Top Language (" + top_language + ")", language_data, language_time
    )

    return markdown


def update_readme(repo, markdown_data, start_marker, end_marker):
    """Updates the README.md file with the provided Markdown content within specified markers"""
    try:
        readme_file = repo.get_contents("README.md")
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
    """Get current README content"""
    readme_file = repo.get_contents("README.md")
    if isinstance(readme_file, list):
        readme_file = readme_file[0]
    return readme_file.decoded_content.decode("utf-8")


def update_wakatime_stats():
    """Function to update Wakatime stats in README"""
    repo = initialize_github()
    if not WAKATIME_API_KEY:
        raise ValueError("WAKATIME_API_KEY environment variable not set")

    # Fetch Wakatime leaderboard data
    leaderboards = get_leaderboards(WAKATIME_API_KEY)

    # Format leaderboard data
    formatted_data = format_leaderboard_data(leaderboards)

    # Define markers
    start_marker = "<!-- Wakatime-Start -->"
    end_marker = "<!-- Wakatime-End -->"

    # Update README content
    new_section_content = update_readme(repo, formatted_data, start_marker, end_marker)

    if new_section_content:
        # Get current README content
        current_readme_content = get_readme_content(repo)

        # Replace the old section with the new one
        start_index = current_readme_content.find(start_marker)
        end_index = current_readme_content.find(end_marker, start_index) + len(
            end_marker
        )
        updated_readme_content = (
            current_readme_content[:start_index]
            + new_section_content
            + current_readme_content[end_index:]
        )

        # Commit changes
        files_to_update = {"README.md": updated_readme_content}
        success = commit_to_github(repo, files_to_update)

        if success:
            logger.info("Updated README with Wakatime Leaderboards")
        else:
            logger.error("Failed to commit changes to GitHub")
    else:
        logger.info("No changes needed in README")


def log_execution_time(start_time):
    """Log the total execution time"""
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
