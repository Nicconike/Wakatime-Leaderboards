"""Test Main Runner Script"""

# Disable pylint warnings for false positives
# pylint: disable=redefined-outer-name, unused-argument
from unittest.mock import patch
import time
import pytest
from api.main import log_execution_time, logger


@pytest.fixture
def mock_dependencies(mocker):
    """Fixtures for mocking dependencies"""
    fixtures = {}
    fixtures["log_execution_time"] = mocker.patch("api.main.log_execution_time")
    fixtures["logger_info"] = mocker.patch.object(logger, "info")
    fixtures["logger_error"] = mocker.patch.object(logger, "error")
    return fixtures


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
