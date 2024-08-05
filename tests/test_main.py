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
        mock_logger.info.assert_any_call(
            "Total Execution Time: %d minutes and %.3f seconds", 1, 5.0
        )

    start_time = time.time() - 30
    with patch("api.main.logger") as mock_logger:
        log_execution_time(start_time)
        mock_logger.info.assert_any_call("Total Execution Time: %.3f seconds", 30.0)
