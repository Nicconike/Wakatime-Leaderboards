"""Main runner script for updating WakaTime leaderboards and badges"""

import os
import logging
import time
from typing import Dict, Optional, Tuple
from dotenv import load_dotenv
from github import GithubException
import requests
from api.wakatime import WakaTimeClient, WakaTimeAPIError
from api.badge_generator import BadgeGenerator, BadgeGenerationConfig, BadgeStyleConfig
from api.data_formatter import extract_stats_summary
from api.markdown_generator import MarkdownGenerator, MarkdownConfig
from api.readme_manager import ReadmeManager
from api.utils import initialize_github, commit_to_github

load_dotenv()

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

README = "README.md"
START_MARKER = "<!-- Wakatime-Start -->"
END_MARKER = "<!-- Wakatime-End -->"

# Version Identifier for Changelog
__version__ = "1.2.4"


def _get_config() -> Tuple[str, str, bool, bool]:
    """Extract configuration from environment variables"""
    wakatime_api_key = os.getenv("INPUT_WAKATIME_API_KEY") or os.getenv(
        "WAKATIME_API_KEY"
    )
    if not wakatime_api_key:
        raise ValueError("WAKATIME_API_KEY not set")

    theme = os.getenv("INPUT_THEME", "default")
    use_badges = os.getenv("INPUT_USE_BADGES", "false").lower() == "true"
    use_tables = os.getenv("INPUT_USE_TABLES", "true").lower() == "true"

    # If USE_TABLES is True, disable badges unless explicitly enabled
    if use_tables and os.getenv("INPUT_USE_BADGES") is None:
        use_badges = False

    # Default to tables if nothing enabled
    if not use_badges and not use_tables:
        use_tables = True

    logger.info(
        "Configuration: USE_TABLES=%s, USE_BADGES=%s, THEME=%s",
        use_tables,
        use_badges,
        theme,
    )

    return wakatime_api_key, theme, use_badges, use_tables


def _initialize_components() -> (
    Tuple[WakaTimeClient, BadgeGenerator, MarkdownGenerator, ReadmeManager]
):
    """Initialize and return all clients & generators"""
    wakatime_api_key, theme, use_badges, use_tables = _get_config()

    # Initialize clients
    repo = initialize_github()
    client = WakaTimeClient(wakatime_api_key)
    badge_style = BadgeStyleConfig.from_theme(theme)
    badges_generator = BadgeGenerator(badge_style)
    markdown_config = MarkdownConfig(use_badges=use_badges, use_tables=use_tables)
    markdown_generator = MarkdownGenerator(markdown_config)
    readme_manager = ReadmeManager(repo, README)

    return client, badges_generator, markdown_generator, readme_manager


def _generate_badge_files(
    badges_generator: BadgeGenerator, leaderboards: dict
) -> Tuple[Dict[str, str], Dict[str, str]]:
    """Generate badge files and return both file paths and content"""
    logger.info("Generating badges...")
    summary = extract_stats_summary(leaderboards)
    badge_config = BadgeGenerationConfig(output_dir="assets")
    badge_content = badges_generator.generate_badge_content(summary, badge_config)

    badge_files = {}
    files_to_commit = {}

    # Map badge content to file paths
    badge_file_mapping = {
        "main": "assets/wakatime-leaderboards.svg",
        "compact": "assets/ranks.svg",
    }

    for badge_type, content in badge_content.items():
        if badge_type in badge_file_mapping:
            file_path = badge_file_mapping[badge_type]
            badge_files[badge_type] = file_path
            files_to_commit[file_path] = content
            logger.info("Added %s to commit", file_path)

    return badge_files, files_to_commit


def _handle_readme_update(
    readme_manager: ReadmeManager, markdown_content: str
) -> Optional[str]:
    """Handle README update and return content if changed"""
    updated_readme = readme_manager.update_readme(
        markdown_content, START_MARKER, END_MARKER
    )
    if updated_readme:
        logger.info("Added README.md to commit")
        return updated_readme
    return None


def _commit_changes(repo, files_to_commit: Dict[str, str]) -> None:
    """Commit all changes to GitHub"""
    if files_to_commit:
        if commit_to_github(repo, files_to_commit):
            logger.info(
                "Successfully committed %s files to GitHub", len(files_to_commit)
            )
        else:
            logger.error("Failed to commit changes to GitHub")
    else:
        logger.info("No changes to commit")


def update_wakatime_leaderboards() -> None:
    """Fetch stats, generate badges and markdown, then update README"""
    # Initialize components
    client, badges_generator, markdown_generator, readme_manager = (
        _initialize_components()
    )
    repo = initialize_github()

    # Fetch stats
    leaderboards = client.get_comprehensive_leaderboards()
    if not leaderboards or leaderboards["total_coding_time"] == 0:
        logger.info("No coding activity detected; skipping update")
        return

    files_to_commit = {}

    # Generate badges if enabled
    if markdown_generator.config.use_badges:
        badge_files, badge_commit_files = _generate_badge_files(
            badges_generator, leaderboards
        )
        files_to_commit.update(badge_commit_files)
    else:
        badge_files = {}

    # Generate markdown content
    markdown_content = markdown_generator.generate_readme_section(
        badge_files, leaderboards
    )

    # Handle README update
    updated_readme = _handle_readme_update(readme_manager, markdown_content)
    if updated_readme:
        files_to_commit[README] = updated_readme

    # Commit all changes
    # _commit_changes(repo, files_to_commit)


def log_execution_time(start_time: float) -> None:
    """Log the total execution time of the script"""
    total_time = round(time.time() - start_time, 3)
    if total_time > 60:
        minutes, seconds = divmod(total_time, 60)
        logger.info(
            "Total Execution Time: %d minutes and %.3f seconds", int(minutes), seconds
        )
    else:
        logger.info("Total Execution Time: %.3f seconds", total_time)


def main():
    """Main Entrypoint"""
    start_time = time.time()
    try:
        update_wakatime_leaderboards()
    except ValueError as ve:
        logger.error("Configuration Error: %s", str(ve))
    except WakaTimeAPIError as we:
        logger.error("WakaTime API error: %s", we)
    except GithubException as ge:
        logger.error("GitHub Error: %s", str(ge))
    except requests.RequestException as re:
        logger.error("Network Error (possibly WakaTime API issue): %s", str(re))
    finally:
        log_execution_time(start_time)


if __name__ == "__main__":
    main()
