"""WakaTime API client for fetching user stats and leaderboards"""

import base64
import math
import time
import logging
from typing import Any, Dict, Optional, Union
import requests

logger = logging.getLogger(__name__)

REQUEST_TIMEOUT = (25, 40)
MAX_RETRIES = 5
BACKOFF_FACTOR = 2
MAX_DELAY = 250
BASE_DELAY = 5


class WakaTimeAPIError(Exception):
    """Exception raised for WakaTime API errors"""


class WakaTimeClient:
    """Client for WakaTime public API"""

    def __init__(self, api_key: str) -> None:
        if not api_key or not api_key.strip():
            raise ValueError("API key is required")
        auth = base64.b64encode(api_key.encode()).decode()
        self.headers = {"Authorization": f"Basic {auth}"}
        self.base_url = "https://wakatime.com/api/v1"

    def _request_with_retries(self, url: str) -> Optional[Dict[str, Any]]:
        delay = BASE_DELAY
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                resp = requests.get(url, headers=self.headers, timeout=REQUEST_TIMEOUT)
                status = resp.status_code
                logger.debug("Attempt %d: HTTP %d %s", attempt, status, url)
                if status == 200:
                    return resp.json().get("data", {})
                if status == 202 or 500 <= status < 600:
                    time.sleep(delay)
                    delay = min(math.ceil(delay * BACKOFF_FACTOR), MAX_DELAY)
                    continue
                if 400 <= status < 500:
                    raise WakaTimeAPIError(f"Client error {status}")
                raise WakaTimeAPIError(f"Unexpected status {status}")
            except (requests.Timeout, requests.ConnectionError) as err:
                if attempt == MAX_RETRIES:
                    raise WakaTimeAPIError(f"Network error: {err}") from err
                time.sleep(delay)
                delay = min(math.ceil(delay * BACKOFF_FACTOR), MAX_DELAY)
        raise WakaTimeAPIError("Max retries reached")

    def get_user_stats(self) -> Optional[Dict[str, Any]]:
        """Get current user's stats for the last 7 days"""
        url = f"{self.base_url}/users/current/stats/last_7_days"
        data = self._request_with_retries(url)
        if not data or data.get("total_seconds", 0) == 0:
            return None
        if not data.get("is_up_to_date", True):
            raise WakaTimeAPIError("Stats not finalized")
        return data

    def get_leaderboard_data(self, language: Optional[str] = None) -> Dict[str, Any]:
        """Get leaderboard data for global or language-specific"""
        url = f"{self.base_url}/leaders"
        if language:
            url += f"?language={language}"
        try:
            resp = requests.get(url, headers=self.headers, timeout=REQUEST_TIMEOUT)
            if resp.status_code == 200:
                return resp.json().get("current_user", {})
            logger.warning("Leaderboard fetch failed: %d", resp.status_code)
            return {}
        except requests.RequestException as err:
            logger.error("Leaderboard request error: %s", err)
            return {}

    def get_comprehensive_leaderboards(
        self,
    ) -> Dict[str, Union[int, str, Dict[str, Any]]]:
        """Combine user stats and leaderboard ranks"""
        stats = self.get_user_stats()
        if stats is None:
            return {
                "total_coding_time": 0,
                "top_language": "",
                "language_times": {},
                "global": {},
                "language": {},
                "current_streak": 0,
            }

        langs = stats.get("languages", [])
        top_lang = langs[0]["name"] if langs else ""
        total = stats.get("total_seconds", 0)
        streak = stats.get("current_streak", {}).get("days", 0)

        return {
            "total_coding_time": total,
            "top_language": top_lang,
            "language_times": {l["name"]: l["total_seconds"] for l in langs},
            "global": self.get_leaderboard_data(),
            "language": self.get_leaderboard_data(top_lang) if top_lang else {},
            "current_streak": streak,
        }
