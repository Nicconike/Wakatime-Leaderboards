"""GitHub API utilities for creating blobs, trees and commits"""

import base64
import logging
import os
from typing import Dict, List
import github
from github import InputGitTreeElement
from github.Repository import Repository

logger = logging.getLogger(__name__)


def get_github_token() -> str:
    """Get GitHub token from environment variables"""
    token = (
        os.getenv("GITHUB_TOKEN")
        or os.getenv("GH_TOKEN")
        or os.getenv("INPUT_GH_TOKEN")
    )
    if not token:
        raise ValueError(
            "No GitHub token found (GITHUB_TOKEN, GH_TOKEN or INPUT_GH_TOKEN)"
        )
    return token


def initialize_github() -> Repository:
    """Initialize GitHub client and return the target repository"""
    token = get_github_token()
    auth = getattr(github, "Auth", None)
    if auth and hasattr(auth, "Token"):
        gh = github.Github(auth=auth.Token(token))
    else:
        gh = github.Github(token)
    repo_name = os.getenv("GITHUB_REPOSITORY")
    if not repo_name:
        raise ValueError("GITHUB_REPOSITORY environment variable not set")
    return gh.get_repo(repo_name)


def create_tree_elements(
    repo: Repository, files_to_update: Dict[str, str]
) -> List[InputGitTreeElement]:
    """Create Git tree elements for each file update"""
    elements: List[InputGitTreeElement] = []
    for path, content in files_to_update.items():
        if isinstance(content, bytes):
            blob_content = base64.b64encode(content).decode("utf-8")
            encoding = "base64"
        else:
            blob_content = content
            encoding = "utf-8"
        blob = repo.create_git_blob(blob_content, encoding)
        element = InputGitTreeElement(
            path=path, mode="100644", type="blob", sha=blob.sha
        )
        elements.append(element)
    return elements


def commit_to_github(repo: Repository, files_to_update: Dict[str, str]) -> bool:
    """Commit files to GitHub repo by creating a new tree and commit"""
    if not files_to_update:
        logger.info("No changes to commit")
        return True

    try:
        default_branch = repo.get_branch(repo.default_branch)
        base_tree = repo.get_git_tree(default_branch.commit.sha)
        tree_elements = create_tree_elements(repo, files_to_update)
        new_tree = repo.create_git_tree(tree_elements, base_tree)
        parent_commit = repo.get_git_commit(default_branch.commit.sha)
        new_commit = repo.create_git_commit(
            message="chore: Update Wakatime badges and stats",
            tree=new_tree,
            parents=[parent_commit],
        )
        repo.get_git_ref(f"heads/{default_branch.name}").edit(sha=new_commit.sha)
        return True
    except (github.GithubException, IOError, ValueError) as err:
        logger.error("Error committing to GitHub: %s", err)
        return False
