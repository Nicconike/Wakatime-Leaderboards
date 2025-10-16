"""SVG Badge generation for WakaTime stats with custom designs"""

import os
import logging
from typing import Dict, Union, Optional
from dataclasses import dataclass

logger = logging.getLogger(__name__)

RANK_COLORS = {
    "top_10": "#48bb78",
    "top_100": "#ed8936",
    "top_1000": "#ecc94b",
    "beyond_1000": "#f56565",
    "unranked": "#718096",
}

BADGE_SIZES = {
    "small": (300, 100),
    "medium": (400, 150),
    "large": (500, 200),
    "compact": (250, 80),
}

THEMES = {
    "default": {"primary": "#667eea", "secondary": "#764ba2", "text": "#ffffff"},
    "dark": {"primary": "#1a1a1a", "secondary": "#2d2d2d", "text": "#ffffff"},
    "github": {"primary": "#24292e", "secondary": "#586069", "text": "#ffffff"},
    "ocean": {"primary": "#0078d4", "secondary": "#106ebe", "text": "#ffffff"},
    "sunset": {"primary": "#ff6b6b", "secondary": "#ffa726", "text": "#ffffff"},
    "forest": {"primary": "#4caf50", "secondary": "#66bb6a", "text": "#ffffff"},
    "purple": {"primary": "#9c27b0", "secondary": "#ba68c8", "text": "#ffffff"},
    "gradient": {"primary": "#667eea", "secondary": "#764ba2", "text": "#ffffff"},
}


@dataclass
class BadgeStyleConfig:
    """Config for badge styling"""

    primary_color: str = "#667eea"
    secondary_color: str = "#764ba2"
    text_color: str = "#ffffff"
    background_opacity: float = 0.1
    border_radius: int = 12
    font_family: str = "Arial, sans-serif"

    @classmethod
    def from_theme(cls, theme_name: str) -> "BadgeStyleConfig":
        """Create style config from theme name"""
        theme = THEMES.get(theme_name.lower(), THEMES["default"])
        return cls(
            primary_color=theme["primary"],
            secondary_color=theme["secondary"],
            text_color=theme["text"],
        )


@dataclass
class StatsRowConfig:
    """Config for a badge stats row"""

    y_pos: int
    label: str
    value: str
    color: str


@dataclass
class StatsSummary:
    """Summary of stats for badge generation"""

    global_rank: str
    language_rank: str
    top_language: str
    total_time: str
    daily_avg: str
    current_streak: int


@dataclass
class BadgeGenerationConfig:
    """Config for badge generation"""

    output_dir: str = "assets"
    size: str = "medium"
    include_main: bool = True
    include_compact: bool = True


class BadgeGenerator:
    """Generate visually appealing SVG badges"""

    def __init__(self, style: Optional[BadgeStyleConfig] = None) -> None:
        self.style = style or BadgeStyleConfig()

    def _get_rank_color(self, rank: Union[str, int]) -> str:
        """Choose color based on rank"""
        try:
            num = int(rank)
        except (TypeError, ValueError):
            return RANK_COLORS["unranked"]

        if num <= 10:
            return RANK_COLORS["top_10"]
        if num <= 100:
            return RANK_COLORS["top_100"]
        if num <= 1000:
            return RANK_COLORS["top_1000"]
        return RANK_COLORS["beyond_1000"]

    def _gradient_defs(self) -> str:
        """Create gradient definitions"""
        primary = self.style.primary_color
        secondary = self.style.secondary_color
        opacity = self.style.background_opacity
        return (
            "<defs>"
            '<linearGradient id="bgG" x1="0%" y1="0%" x2="100%" y2="100%">'
            f'<stop offset="0%" style="stop-color:{primary};stop-opacity:1"/>'
            f'<stop offset="100%" style="stop-color:{secondary};stop-opacity:1"/>'
            "</linearGradient>"
            '<linearGradient id="cardBg" x1="0%" y1="0%" x2="100%" y2="100%">'
            f'<stop offset="0%" style="stop-color:rgba(255,255,255,{opacity});stop-opacity:1"/>'
            f'<stop offset="100%" style="stop-color:rgba(255,255,255,{opacity/2});stop-opacity:1"/>'
            "</linearGradient>"
            "</defs>"
        )

    def _row_svg(self, cfg: StatsRowConfig) -> str:
        """Render one stats row"""
        font_family = self.style.font_family
        text_color = self.style.text_color
        return (
            f'<circle cx="35" cy="{cfg.y_pos-5}" r="6" fill="{cfg.color}"/>'
            f'<text x="50" y="{cfg.y_pos}" font-family="{font_family}" '
            f'font-size="14" fill="{text_color}" font-weight="500">{cfg.label}: </text>'
            f'<text x="180" y="{cfg.y_pos}" font-family="{font_family}" '
            f'font-size="14" fill="{text_color}" font-weight="bold">{cfg.value}</text>'
        )

    def _extract_stats(self, stats: Dict[str, Union[str, int]]) -> StatsSummary:
        gr = str(stats.get("global_rank", "0"))
        lr = str(stats.get("language_rank", "0"))
        tl = str(stats.get("top_language", "Unknown"))[:12]
        tt = str(stats.get("formatted_total_time", "0 mins"))
        da = str(stats.get("daily_avg", "0 mins"))
        cs = int(stats.get("current_streak", 0))
        return StatsSummary(gr, lr, tl, tt, da, cs)

    def _create_rows(self, summary: StatsSummary) -> str:
        rows = [
            StatsRowConfig(
                70,
                "Global Rank",
                f"#{summary.global_rank}",
                self._get_rank_color(summary.global_rank),
            ),
            StatsRowConfig(
                100,
                f"{summary.top_language} Rank",
                f"#{summary.language_rank}",
                self._get_rank_color(summary.language_rank),
            ),
            StatsRowConfig(130, "Total Coded", summary.total_time, "#f6ad55"),
            StatsRowConfig(160, "Daily Avg", summary.daily_avg, "#9f7aea"),
            StatsRowConfig(
                190,
                "Streak",
                f"{summary.current_streak} day{'s' if summary.current_streak != 1 else ''}",
                "#ff6b6b" if summary.current_streak > 0 else "#718096",
            ),
        ]
        return "".join(self._row_svg(r) for r in rows)

    def generate_main_card(
        self, stats: Dict[str, Union[str, int]], config: BadgeGenerationConfig
    ) -> str:
        """Generate comprehensive stats card SVG"""
        w, h = BADGE_SIZES.get(config.size, BADGE_SIZES["medium"])
        summary = self._extract_stats(stats)
        rows_svg = self._create_rows(summary)

        br, ff, tc = (
            self.style.border_radius,
            self.style.font_family,
            self.style.text_color,
        )
        svg = (
            f"<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}'>"
            + self._gradient_defs()
            + f"<rect width='100%' height='100%' fill='url(#bgG)' rx='{br}'/>"
            + f"<rect x='10' y='10' width='{w-20}' height='{h-20}' fill='url(#cardBg)' rx='{
                br-4}' stroke='rgba(255,255,255,0.2)' stroke-width='1'/>"
            + f"<text x='25' y='40' font-family='{ff}' font-size='18' font-weight='bold' fill='{
                tc}'>📊 WakaTime Weekly Stats</text>"
            + rows_svg
            + "</svg>"
        )
        return svg

    def generate_compact(self, stats: Dict[str, Union[str, int]]) -> str:
        """Generate compact rank-only badge SVG"""
        w, h = BADGE_SIZES["compact"]
        summary = self._extract_stats(stats)

        br, ff, tc = (
            self.style.border_radius // 2,
            self.style.font_family,
            self.style.text_color,
        )
        svg = (
            f"<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}'>"
            + "<defs><linearGradient id='cg' x1='0%' y1='0%' x2='100%' y2='0%'>"
            + "<stop offset='0%' style='stop-color:#4facfe;stop-opacity:1'/>"
            + "<stop offset='100%' style='stop-color:#00f2fe;stop-opacity:1'/>"
            + "</linearGradient></defs>"
            + f"<rect width='100%' height='100%' fill='url(#cg)' rx='{br}'/>"
            + f"<rect x='5' y='15' width='{w//2-10}' height='{
                h-30}' fill='rgba(255,255,255,0.1)' rx='6'/>"
            + f"<text x='15' y='35' font-family='{ff}' font-size='10' fill='{
                tc}' font-weight='500'>Global</text>"
            + f"<text x='15' y='55' font-family='{ff}' font-size='14' fill='{
                tc}' font-weight='bold'>#{summary.global_rank}</text>"
            + f"<rect x='{w//2+5}' y='15' width='{w//2-10}' height='{
                h-30}' fill='rgba(255,255,255,0.1)' rx='6'/>"
            + f"<text x='{w//2+15}' y='35' font-family='{ff}' font-size='10' fill='{
                tc}' font-weight='500'>{summary.top_language[:8]}</text>"
            + f"<text x='{w//2+15}' y='55' font-family='{ff}' font-size='14' fill='{
                tc}' font-weight='bold'>#{summary.language_rank}</text>"
            + "</svg>"
        )
        return svg

    def generate_badge_content(
        self, stats: Dict[str, Union[str, int]], config: BadgeGenerationConfig
    ) -> Dict[str, str]:
        """Generate badge content as strings for GitHub commit"""
        content = {}

        if config.include_main:
            content["main"] = self.generate_main_card(stats, config)
            logger.info("Generated main badge content")

        if config.include_compact:
            content["compact"] = self.generate_compact(stats)
            logger.info("Generated compact badge content")

        return content

    def write_badges(
        self, stats: Dict[str, Union[str, int]], config: BadgeGenerationConfig
    ) -> Dict[str, str]:
        """Generate and write badge SVG files, returning file paths"""
        os.makedirs(config.output_dir, exist_ok=True)
        paths: Dict[str, str] = {}

        badge_content = self.generate_badge_content(stats, config)

        if "main" in badge_content:
            main_svg = badge_content["main"]
            main_path = f"{config.output_dir}/wakatime-leaderboards.svg"
            with open(main_path, "w", encoding="utf-8") as file_handle:
                file_handle.write(main_svg)
            paths["main"] = main_path

        if "compact" in badge_content:
            comp_svg = badge_content["compact"]
            comp_path = f"{config.output_dir}/ranks.svg"
            with open(comp_path, "w", encoding="utf-8") as file_handle:
                file_handle.write(comp_svg)
            paths["compact"] = comp_path

        logger.info("Badges written: %s", list(paths.values()))
        return paths
