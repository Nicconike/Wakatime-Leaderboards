"""Test Main Runner Script"""

# Disable pylint warnings for false positives
# pylint: disable=redefined-outer-name, unused-argument
from unittest.mock import patch, MagicMock
import time
import pytest
from github import GithubException
import requests
from api.main import (
    format_time,
    get_wakatime_stats,
    get_leaderboards,
    format_leaderboard_data,
    update_readme,
    get_readme_content,
    update_wakatime_stats,
    main,
    log_execution_time,
    logger,
    README,
)


@pytest.fixture
def mock_dependencies(mocker):
    """Fixtures for mocking dependencies"""
    fixtures = {}
    fixtures["log_execution_time"] = mocker.patch("api.main.log_execution_time")
    fixtures["logger_info"] = mocker.patch.object(logger, "info")
    fixtures["logger_error"] = mocker.patch.object(logger, "error")
    return fixtures


@patch("api.main.WAKATIME_API_KEY", None)
def test_handle_no_wakatime_api_key():
    """Test when WAKATIME_API_KEY is not set."""
    with pytest.raises(
        ValueError, match="WAKATIME_API_KEY environment variable not set"
    ):
        update_wakatime_stats()


def test_format_time():
    """Test format_time function"""
    if format_time(60) != "1 min":
        pytest.fail("Expected '1 min' for 60 seconds")
    if format_time(120) != "2 mins":
        pytest.fail("Expected '2 mins' for 120 seconds")

    if format_time(3600) != "1 hr":
        pytest.fail("Expected '1 hr' for 3600 seconds")
    if format_time(7200) != "2 hrs":
        pytest.fail("Expected '2 hrs' for 7200 seconds")
    if format_time(10800) != "3 hrs":
        pytest.fail("Expected '3 hrs' for 10800 seconds")

    if format_time(3661) != "1 hr 1 min":
        pytest.fail("Expected '1 hr 1 min' for 3661 seconds")
    if format_time(7261) != "2 hrs 1 min":
        pytest.fail("Expected '2 hrs 1 min' for 7261 seconds")
    if format_time(3720) != "1 hr 2 mins":
        pytest.fail("Expected '1 hr 2 mins' for 3720 seconds")

    if format_time(3599) != "59 mins":
        pytest.fail("Expected '59 mins' for 3599 seconds")


@patch("api.main.requests.get")
def test_get_wakatime_stats(mock_get):
    """Test get_wakatime_stats function"""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"data": {"total_seconds": 3600}}
    mock_get.return_value = mock_response

    result = get_wakatime_stats("fake_api_key")
    if result != {"total_seconds": 3600}:
        pytest.fail("Unexpected result from get_wakatime_stats")

    mock_response.json.return_value = {"data": {"total_seconds": 0}}
    result = get_wakatime_stats("fake_api_key")
    if result is not None:
        pytest.fail("Expected None for zero total_seconds")

    mock_response.status_code = 404
    mock_get.return_value = mock_response
    try:
        get_wakatime_stats("fake_api_key")
        pytest.fail("Expected ValueError was not raised")
    except ValueError as e:
        if str(e) != "Failed to fetch user stats: 404":
            pytest.fail("Unexpected error message: " + str(e))


@patch("api.main.get_wakatime_stats")
@patch("api.main.requests.get")
def test_get_leaderboards(mock_get, mock_get_stats):
    """Test get_leaderboards function"""
    mock_get_stats.return_value = {
        "total_seconds": 3600,
        "languages": [{"name": "Python", "total_seconds": 3600}],
    }
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"current_user": {"rank": 1}}
    mock_get.return_value = mock_response

    result = get_leaderboards("fake_api_key")
    if result["total_coding_time"] != 3600 or result["top_language"] != "Python":
        pytest.fail("Unexpected result from get_leaderboards")
    if "global" not in result or result["global"] != {"rank": 1}:
        pytest.fail("Unexpected global data in result")

    mock_get_stats.return_value = None
    result = get_leaderboards("fake_api_key")
    expected_result = {
        "total_coding_time": 0,
        "top_language": None,
        "language_times": {},
        "global": {},
        "language": {},
    }
    if result != expected_result:
        pytest.fail("Unexpected result when stats are None")

    mock_get_stats.return_value = {
        "total_seconds": 3600,
        "languages": [{"name": "Python", "total_seconds": 3600}],
    }
    mock_response.status_code = 404
    result = get_leaderboards("fake_api_key")
    if "global" in result:
        pytest.fail("Expected 'global' key to be absent on API error")
    if result["total_coding_time"] != 3600 or result["top_language"] != "Python":
        pytest.fail("Unexpected result from get_leaderboards on API error")


def test_format_leaderboard_data():
    """Test format_leaderboard_data function"""
    leaderboards = {
        "total_coding_time": 3600,
        "top_language": "Python",
        "language_times": {"Python": 3600},
        "global": {"rank": 1},
        "language": {"rank": 2},
    }
    result = format_leaderboard_data(leaderboards)
    if "Public Leaderboards (Weekly)" not in result:
        pytest.fail("Missing Public Leaderboards section")
    if "Top Language (Python)" not in result:
        pytest.fail("Missing Top Language section")
    if "| 1 | 1 hr | 8 mins |" not in result:
        pytest.fail("Incorrect global rank or time formatting")
    if "| 2 | 1 hr | 8 mins |" not in result:
        pytest.fail("Incorrect language rank or time formatting")

    # Test case for no coding activity
    no_activity_leaderboards = {
        "total_coding_time": 0,
        "top_language": None,
        "language_times": {},
        "global": {},
        "language": {},
    }
    no_activity_result = format_leaderboard_data(no_activity_leaderboards)
    if "No coding activity detected in the past week." not in no_activity_result:
        pytest.fail("Missing no coding activity message")


def test_update_readme():
    """Test update_readme function with all scenarios"""
    # Test when markers exist and content needs updating
    mock_repo = MagicMock()
    mock_file = MagicMock()
    mock_file.decoded_content.decode.return_value = (
        "<!-- Wakatime-Start -->\nOld content\n<!-- Wakatime-End -->"
    )
    mock_repo.get_contents.return_value = mock_file

    result = update_readme(
        mock_repo, "New content", "<!-- Wakatime-Start -->", "<!-- Wakatime-End -->"
    )
    if result != "<!-- Wakatime-Start -->\nNew content\n<!-- Wakatime-End -->":
        pytest.fail("Unexpected result when markers exist and content needs updating")

    # Test when markers exist but content doesn't need updating
    mock_file.decoded_content.decode.return_value = (
        "<!-- Wakatime-Start -->\nNew content\n<!-- Wakatime-End -->"
    )
    result = update_readme(
        mock_repo, "New content", "<!-- Wakatime-Start -->", "<!-- Wakatime-End -->"
    )
    if result is not None:
        pytest.fail("Expected None when content doesn't need updating")

    # Test when start marker is not found
    mock_file.decoded_content.decode.return_value = (
        "<!-- Wakatime-End -->\nOld content\n<!-- Wakatime-End -->"
    )
    result = update_readme(
        mock_repo, "New content", "<!-- Wakatime-Start -->", "<!-- Wakatime-End -->"
    )
    if result is not None:
        pytest.fail("Expected None when start marker is not found")

    # Test when end marker is not found
    mock_file.decoded_content.decode.return_value = (
        "<!-- Wakatime-Start -->\nOld content\n"
    )
    result = update_readme(
        mock_repo, "New content", "<!-- Wakatime-Start -->", "<!-- Wakatime-End -->"
    )
    if result is not None:
        pytest.fail("Expected None when end marker is not found")

    # Test when an exception occurs
    mock_repo.get_contents.side_effect = FileNotFoundError("File not found")
    result = update_readme(
        mock_repo, "New content", "<!-- Wakatime-Start -->", "<!-- Wakatime-End -->"
    )
    if result is not None:
        pytest.fail("Expected None when an exception occurs")

    # Test logger error messages
    with patch.object(logger, "error") as mock_logger:
        mock_repo.get_contents.side_effect = FileNotFoundError("File not found")
        update_readme(
            mock_repo, "New content", "<!-- Wakatime-Start -->", "<!-- Wakatime-End -->"
        )
        mock_logger.assert_called_with(
            "Error occurred while updating README: %s", "File not found"
        )

    with patch.object(logger, "error") as mock_logger:
        mock_repo.get_contents.side_effect = None
        mock_file.decoded_content.decode.return_value = "No markers here"
        update_readme(
            mock_repo, "New content", "<!-- Wakatime-Start -->", "<!-- Wakatime-End -->"
        )
        mock_logger.assert_called_with(
            "Markers not found: %s", "<!-- Wakatime-Start -->"
        )


def test_get_readme_content():
    """Test get_readme_content function"""
    # Test when get_contents returns a single file
    mock_repo = MagicMock()
    mock_file = MagicMock()
    mock_file.decoded_content.decode.return_value = "Single README content"
    mock_repo.get_contents.return_value = mock_file

    result = get_readme_content(mock_repo)
    if result != "Single README content":
        pytest.fail("Unexpected result when get_contents returns a single file")

    # Test when get_contents returns a list of files
    mock_file_list = [MagicMock()]
    mock_file_list[0].decoded_content.decode.return_value = "List README content"
    mock_repo.get_contents.return_value = mock_file_list

    result = get_readme_content(mock_repo)
    if result != "List README content":
        pytest.fail("Unexpected result when get_contents returns a list of files")

    # Test that the correct README constant is used
    mock_repo.get_contents.reset_mock()
    mock_repo.get_contents.return_value = mock_file
    get_readme_content(mock_repo)
    mock_repo.get_contents.assert_called_once_with(README)


@patch("api.main.initialize_github")
@patch("api.main.get_leaderboards")
@patch("api.main.format_leaderboard_data")
@patch("api.main.update_readme")
@patch("api.main.get_readme_content")
@patch("api.main.commit_to_github")
@patch("api.main.logger")
def test_update_wakatime_stats(
    mock_logger,
    mock_commit,
    mock_get_readme,
    mock_update,
    mock_format,
    mock_get_leaderboards,
    mock_init,
):
    """Test update_wakatime_stats function"""

    # Setup
    mock_repo = MagicMock()
    mock_init.return_value = mock_repo

    # Test case: Normal flow with updates
    mock_get_leaderboards.return_value = {"total_coding_time": 3600}
    mock_format.return_value = "Formatted data"
    mock_update.return_value = "New section"
    mock_get_readme.return_value = "Old README"
    mock_commit.return_value = True

    update_wakatime_stats()

    if not mock_commit.called:
        pytest.fail("commit_to_github was not called when it should have been")
    mock_logger.info.assert_called_with("Updated README with Wakatime Leaderboards")

    # Reset mocks
    mock_logger.reset_mock()
    mock_commit.reset_mock()
    mock_get_readme.reset_mock()
    mock_update.reset_mock()
    mock_format.reset_mock()
    mock_get_leaderboards.reset_mock()

    # Test case: No coding activity
    mock_get_leaderboards.return_value = {"total_coding_time": 0}

    update_wakatime_stats()

    mock_logger.info.assert_called_with("No coding activity detected in the past week.")
    if mock_update.called or mock_get_readme.called or mock_commit.called:
        pytest.fail(
            "Unexpected functions were called when no coding activity was detected"
        )

    # Reset mocks
    mock_logger.reset_mock()
    mock_commit.reset_mock()
    mock_get_readme.reset_mock()
    mock_update.reset_mock()
    mock_format.reset_mock()
    mock_get_leaderboards.reset_mock()

    # Test case: No changes needed in README
    mock_get_leaderboards.return_value = {"total_coding_time": 3600}
    mock_update.return_value = None

    update_wakatime_stats()

    mock_logger.info.assert_called_with("No changes needed in README")
    if mock_commit.called:
        pytest.fail("commit_to_github was called when no changes were needed")

    # Reset mocks
    mock_logger.reset_mock()
    mock_commit.reset_mock()
    mock_get_readme.reset_mock()
    mock_update.reset_mock()
    mock_format.reset_mock()
    mock_get_leaderboards.reset_mock()

    # Test case: Failed to retrieve README content
    mock_get_leaderboards.return_value = {"total_coding_time": 3600}
    mock_update.return_value = "New section"
    mock_get_readme.return_value = None

    update_wakatime_stats()

    mock_logger.error.assert_called_with("Failed to retrieve README content.")
    if mock_commit.called:
        pytest.fail("commit_to_github was called when README content retrieval failed")

    # Reset mocks
    mock_logger.reset_mock()
    mock_commit.reset_mock()
    mock_get_readme.reset_mock()
    mock_update.reset_mock()
    mock_format.reset_mock()
    mock_get_leaderboards.reset_mock()

    # Test case: Failed to commit changes
    mock_get_leaderboards.return_value = {"total_coding_time": 3600}
    mock_update.return_value = "New section"
    mock_get_readme.return_value = "Old README"
    mock_commit.return_value = False

    update_wakatime_stats()

    mock_logger.error.assert_called_with("Failed to commit changes to GitHub")

    # Test case: WAKATIME_API_KEY not set
    with patch("api.main.WAKATIME_API_KEY", None):
        with pytest.raises(
            ValueError, match="WAKATIME_API_KEY environment variable not set"
        ):
            update_wakatime_stats()


def test_log_execution_time():
    """Test Log execution time"""
    start_time = time.time() - 65
    with patch("api.main.logger") as mock_logger:
        log_execution_time(start_time)
        calls = mock_logger.info.call_args_list
        if len(calls) != 1:
            pytest.fail("Expected 1 call to logger.info, got " + str(len(calls)))
        args, _ = calls[0]
        if args[0] != "Total Execution Time: %d minutes and %.3f seconds":
            pytest.fail("Unexpected log format")
        if args[1] != 1:
            pytest.fail("Expected 1 minute, got " + str(args[1]))
        if abs(args[2] - 5.0) >= 0.1:
            pytest.fail("Expected approximately 5.0 seconds, got " + str(args[2]))

    start_time = time.time() - 30
    with patch("api.main.logger") as mock_logger:
        log_execution_time(start_time)
        calls = mock_logger.info.call_args_list
        if len(calls) != 1:
            pytest.fail("Expected 1 call to logger.info, got " + str(len(calls)))
        args, _ = calls[0]
        if args[0] != "Total Execution Time: %.3f seconds":
            pytest.fail("Unexpected log format")
        if abs(args[1] - 30.0) >= 0.1:
            pytest.fail("Expected approximately 30.0 seconds, got " + str(args[1]))


@patch("api.main.time.time")
@patch("api.main.update_wakatime_stats")
@patch("api.main.log_execution_time")
@patch("api.main.logger")
def test_main(
    mock_logger, mock_log_execution_time, mock_update_wakatime_stats, mock_time
):
    """Test main function"""

    # Set up mock time
    mock_time.return_value = 1000

    # Test normal execution
    main()
    if not mock_update_wakatime_stats.called:
        pytest.fail("update_wakatime_stats was not called")
    if not mock_log_execution_time.called:
        pytest.fail("log_execution_time was not called")
    mock_log_execution_time.assert_called_with(1000)

    # Test ValueError
    mock_update_wakatime_stats.side_effect = ValueError("Test ValueError")
    main()
    mock_logger.error.assert_called_with("Value Error: %s", "Test ValueError")
    if not mock_log_execution_time.called:
        pytest.fail("log_execution_time was not called after ValueError")

    # Test GithubException
    mock_update_wakatime_stats.side_effect = GithubException(
        500, "Test GithubException"
    )
    main()
    mock_logger.error.assert_called_with(
        "GitHub Error: %s", '500 "Test GithubException"'
    )
    if not mock_log_execution_time.called:
        pytest.fail("log_execution_time was not called after GithubException")

    # Test RequestException
    mock_update_wakatime_stats.side_effect = requests.RequestException(
        "Test RequestException"
    )
    main()
    mock_logger.error.assert_called_with(
        "Request Error (possibly WakaTime API issue): %s", "Test RequestException"
    )
    if not mock_log_execution_time.called:
        pytest.fail("log_execution_time was not called after RequestException")

    # Test IOError
    mock_update_wakatime_stats.side_effect = IOError("Test IOError")
    main()
    mock_logger.error.assert_called_with("I/O Error: %s", "Test IOError")
    if not mock_log_execution_time.called:
        pytest.fail("log_execution_time was not called after IOError")

    # Test KeyError
    mock_update_wakatime_stats.side_effect = KeyError("Test KeyError")
    main()
    mock_logger.error.assert_called_with(
        "Key Error (possibly missing data in API response): %s", "'Test KeyError'"
    )
    if not mock_log_execution_time.called:
        pytest.fail("log_execution_time was not called after KeyError")

    # Verify total call counts
    if mock_update_wakatime_stats.call_count != 6:
        pytest.fail("update_wakatime_stats was not called 6 times")
    if mock_log_execution_time.call_count != 6:
        pytest.fail("log_execution_time was not called 6 times")
