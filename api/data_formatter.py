"""Data formatting utilities for WakaTime stats.

This module provides utility functions for formatting time durations,
calculating averages and extracting key statistics from WakaTime data.
"""

from typing import Dict, Union, Any, Optional


def format_time(seconds: Union[int, float]) -> str:
    """Format time duration to human-readable format"""
    if seconds < 0:
        return "0 seconds"

    hours, remainder = divmod(int(seconds), 3600)
    minutes, _ = divmod(remainder, 60)

    if hours == 0:
        if minutes == 0:
            return "0 mins"
        if minutes == 1:
            return "1 min"
        return f"{minutes} mins"

    if minutes == 0:
        return f"{hours} hr{'s' if hours != 1 else ''}"

    return (
        f"{hours} hr{'s' if hours != 1 else ''} "
        f"{minutes} min{'s' if minutes > 1 else ''}"
    )


def calculate_daily_average(total_seconds: int, days: int = 7) -> str:
    """Calculate and format daily average coding time"""
    if days <= 0:
        raise ValueError("Days must be positive")
    return format_time(total_seconds / days)


def extract_stats_summary(leaderboards: Dict[str, Any]) -> Dict[str, Union[str, int]]:
    """Extract key stats for badge generation from leaderboard data.

    Args:
        leaderboards: Comprehensive leaderboard data dictionary

    Returns:
        Dictionary containing summarized stats for badge generation
    """
    total_time = leaderboards.get("total_coding_time", 0)

    return {
        "global_rank": leaderboards.get("global", {}).get("rank", "-"),
        "language_rank": leaderboards.get("language", {}).get("rank", "-"),
        "top_language": leaderboards.get("top_language", "Unknown"),
        "total_time": total_time,
        "daily_avg": calculate_daily_average(total_time),
        "formatted_total_time": format_time(total_time),
        "current_streak": leaderboards.get("current_streak", 0),
    }


def get_rank_display_text(rank: Union[str, int, None]) -> str:
    """Get display text for rank with proper formatting.

    Args:
        rank: Rank value (can be string, int, or None)

    Returns:
        Formatted rank display text
    """
    if rank is None or rank == "-" or rank == "":
        return "Unranked"

    try:
        rank_num = int(rank)
        return f"#{rank_num}"
    except (ValueError, TypeError):
        return "Unranked"


def get_language_display_name(
    language: Optional[str] = None, max_length: int = 12
) -> str:
    """Get properly formatted language name for display"""
    if not language or language.lower() == "unknown":
        return "Unknown"

    # Truncate long language names
    if len(language) > max_length:
        return f"{language[:max_length-1]}…"

    return language


def calculate_coding_consistency(total_seconds: int, days: int = 7) -> str:
    """Calculate coding consistency level based on daily average"""
    if days <= 0:
        return "Unknown"

    daily_avg_hours = (total_seconds / days) / 3600

    consistency_levels = [
        (8, "🔥 Highly Active"),
        (4, "💪 Very Active"),
        (2, "👍 Active"),
        (1, "📈 Moderate"),
        (0.01, "🌱 Getting Started"),
    ]

    for threshold, level in consistency_levels:
        if daily_avg_hours >= threshold:
            return level

    return "😴 Inactive"
