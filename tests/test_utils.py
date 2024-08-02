"""Test utils Runner Script"""
# Disable pylint warnings for false positives
# pylint: disable=redefined-outer-name, unused-argument
import os
from unittest import TestCase
from unittest.mock import patch, MagicMock
import pytest
from api.utils import (get_github_token, get_repo,
                       initialize_github, create_tree_elements, commit_to_github, logger)


@pytest.fixture
def mock_repo():
    """Mock Repo"""
    return MagicMock()


@pytest.fixture
def mock_github():
    """Mock Github Repo"""
    with patch("api.utils.Github") as mock_github:
        yield mock_github


@pytest.fixture
def mock_env_vars(monkeypatch):
    """Mock environment variables"""
    monkeypatch.setenv("GITHUB_TOKEN", "fake_token")
    monkeypatch.setenv("GITHUB_REPOSITORY", "fake/repo")
    monkeypatch.setenv("INPUT_WAKATIME_API_KEY", "fake_wakatime_api_key")


@pytest.fixture
def mock_dependencies(mocker):
    """Fixtures for mocking dependencies"""
    fixtures = {}
    fixtures['initialize_github'] = mocker.patch('api.utils.initialize_github')
    fixtures['collect_files_to_update'] = mocker.patch(
        'api.utils.collect_files_to_update')
    fixtures['commit_to_github'] = mocker.patch('api.utils.commit_to_github')
    fixtures['logger_info'] = mocker.patch.object(logger, 'info')
    fixtures['logger_error'] = mocker.patch.object(logger, 'error')
    return fixtures


def test_get_github_token(mock_env_vars):
    """Test fetching github token"""
    token = get_github_token()
    TestCase().assertEqual(token, "fake_token")

    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValueError, match="No GitHub token found in env vars"):
            get_github_token()


def test_get_repo(mock_github):
    """Test fetching GitHub repo"""
    mock_repo = MagicMock()
    mock_github.return_value.get_repo.return_value = mock_repo

    with patch.dict(os.environ, {"GITHUB_REPOSITORY": "fake/repo"}):
        repo = get_repo(mock_github.return_value)
        TestCase().assertEqual(repo, mock_repo)

    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValueError, match="GITHUB_REPOSITORY environment variable not set"):
            get_repo(mock_github.return_value)


def test_initialize_github(mock_github, mock_env_vars):
    """Test Initializing Github Repo"""
    mock_repo = MagicMock()
    mock_github.return_value.get_repo.return_value = mock_repo

    repo = initialize_github()
    TestCase().assertEqual(repo, mock_repo)


@patch("api.utils.InputGitTreeElement")
def test_create_tree_elements(mock_input_git_tree_element, mock_repo):
    """Test Create Tree elements"""
    files_to_update = {
        "README.md": "New Content",
        "image.png": b"binary content"
    }
    mock_repo.create_git_blob.side_effect = lambda content, encoding: MagicMock(
        sha="fake_sha")
    mock_input_git_tree_element.side_effect = lambda path, mode, type, sha: MagicMock(
        path=path)

    tree_elements = create_tree_elements(mock_repo, files_to_update)

    TestCase().assertEqual(len(tree_elements), 2)
    TestCase().assertEqual(tree_elements[0].path, "README.md")
    TestCase().assertEqual(tree_elements[1].path, "image.png")


@patch("api.utils.create_tree_elements")
@patch("api.utils.logger")
def test_commit_to_github(mock_logger, mock_create_tree_elements, mock_repo):
    """Test Committing to Github Repo"""
    mock_create_tree_elements.return_value = [MagicMock()]
    mock_repo.get_branch.return_value.commit.sha = "fake_sha"
    mock_repo.create_git_tree.return_value = MagicMock()
    mock_repo.create_git_commit.return_value = MagicMock(sha="new_commit_sha")
    mock_repo.get_git_ref.return_value.edit.return_value = None

    result = commit_to_github(mock_repo, {"README.md": "New Content"})
    TestCase().assertTrue(result)

    result = commit_to_github(mock_repo, {})
    TestCase().assertTrue(result)

    mock_repo.get_branch.side_effect = ValueError("Test ValueError")
    result = commit_to_github(mock_repo, {"README.md": "New Content"})
    TestCase().assertFalse(result)
    mock_logger.error.assert_any_call(
        "Error occurred while committing to GitHub: %s", "Test ValueError")

    mock_repo.get_branch.side_effect = IOError("Test IOError")
    result = commit_to_github(mock_repo, {"README.md": "New Content"})
    TestCase().assertFalse(result)
    mock_logger.error.assert_any_call(
        "Error occurred while committing to GitHub: %s", "Test IOError")
