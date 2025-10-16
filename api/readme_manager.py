"""Manage updating the README file with new WakaTime sections"""

import logging
from typing import Optional
from github.Repository import Repository

logger = logging.getLogger(__name__)


class ReadmeManager:
    """Handles fetching and updating README content for GitHub commits"""

    def __init__(self, repo: Repository, path: str = "README.md") -> None:
        self.repo = repo
        self.path = path

    def update_readme(
        self, markdown_data: str, start_marker: str, end_marker: str
    ) -> Optional[str]:
        """Returns the updated README content if changes are needed"""
        try:
            contents = self.repo.get_contents(self.path)
            if isinstance(contents, list):
                readme_file = contents[0]
            else:
                readme_file = contents
            current_readme = readme_file.decoded_content.decode("utf-8")

            start_index = current_readme.find(start_marker)
            end_index = current_readme.find(end_marker, start_index)

            if start_index == -1 or end_index == -1:
                logger.error("Markers not found: %s or %s", start_marker, end_marker)
                return None

            new_section_content = (
                start_marker + "\n" + markdown_data + "\n" + end_marker
            )

            # Extract current section for comparison
            current_section = current_readme[start_index : end_index + len(end_marker)]

            # Check if content actually changed
            if new_section_content == current_section:
                logger.info("README content unchanged, skipping update")
                return None

            # Build complete updated README
            updated_readme = (
                current_readme[:start_index]
                + new_section_content
                + current_readme[end_index + len(end_marker) :]
            )

            logger.info("README content updated successfully")
            return updated_readme

        except (FileNotFoundError, PermissionError, IOError) as e:
            logger.error("Error occurred while updating README: %s", str(e))
            return None
