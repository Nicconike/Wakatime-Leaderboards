"""Github API utilities"""

import base64
import logging
import os
from github import Github, InputGitTreeElement

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def get_github_token():
    """Get GitHub token from environment variables"""
    token = (
        os.environ.get("GITHUB_TOKEN")
        or os.environ.get("GH_TOKEN")
        or os.environ.get("INPUT_GH_TOKEN")
    )
    if not token:
        raise ValueError(
            "No GitHub token found in env vars (GITHUB_TOKEN, GH_TOKEN or INPUT_GH_TOKEN"
        )
    return token


def get_repo(g):
    """Get Repo object"""
    repo_name = os.environ.get("GITHUB_REPOSITORY")
    if not repo_name:
        raise ValueError("GITHUB_REPOSITORY environment variable not set")
    return g.get_repo(repo_name)


def initialize_github():
    """Initialize GitHub client and get repo"""
    token = get_github_token()
    g = Github(token)
    return get_repo(g)


def create_tree_elements(repo, files_to_update):
    """Create tree elements for GitHub commit"""
    tree_elements = []
    for file_path, file_content in files_to_update.items():
        if isinstance(file_content, bytes):
            content = base64.b64encode(file_content).decode("utf-8")
            encoding = "base64"
        else:
            content = file_content
            encoding = "utf-8"

        blob = repo.create_git_blob(content, encoding)
        element = InputGitTreeElement(
            path=file_path, mode="100644", type="blob", sha=blob.sha
        )
        tree_elements.append(element)
    return tree_elements


def commit_to_github(repo, files_to_update):
    """Commit files to GitHub Repo"""
    if not files_to_update:
        logger.info("No changes to commit")
        return True

    try:
        branch = repo.get_branch(repo.default_branch)
        last_commit_sha = branch.commit.sha

        tree_elements = create_tree_elements(repo, files_to_update)
        new_tree = repo.create_git_tree(
            tree_elements, repo.get_git_tree(last_commit_sha)
        )

        new_commit = repo.create_git_commit(
            message="chore: Update Wakatime Leaderboards",
            tree=new_tree,
            parents=[repo.get_git_commit(last_commit_sha)],
        )

        ref = repo.get_git_ref("heads/" + branch.name)
        ref.edit(sha=new_commit.sha)
        return True

    except (ValueError, IOError) as e:
        logger.error("Error occurred while committing to GitHub: %s", str(e))
        return False
