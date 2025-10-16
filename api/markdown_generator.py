"""Generate markdown content for README injection"""

from typing import Any, Dict, List
from dataclasses import dataclass


@dataclass
class MarkdownConfig:
    """Configuration for markdown generation"""

    badge_folder: str = "assets"
    use_badges: bool = True
    use_tables: bool = True
    title: str = "📊 WakaTime Weekly Stats"


class MarkdownGenerator:
    """Generate markdown sections with badges and tables"""

    def __init__(self, config: MarkdownConfig = MarkdownConfig()) -> None:
        self.config = config

    def generate_badge_section(self, badge_paths: Dict[str, str]) -> str:
        """Generate markdown for badge images"""
        lines: List[str] = [f"### {self.config.title}", ""]
        if "main" in badge_paths and self.config.use_badges:
            lines.append(f"![WakaTime Stats]({badge_paths['main']})")
        if "compact" in badge_paths and self.config.use_badges:
            lines.append(f"![Ranks]({badge_paths['compact']})")
        lines.append("")
        return "\n".join(lines)

    def generate_table_section(self, leaderboards: Dict[str, Any]) -> str:
        """Generate traditional markdown tables"""
        if not self.config.use_tables:
            return ""

        total_seconds = leaderboards.get("total_coding_time", 0)
        if total_seconds == 0:
            return "No coding activity detected this week.\n"

        def build_table(header: str, data: Dict[str, Any]) -> str:
            """Helper to build one markdown table"""
            return (
                f"#### {header}\n\n"
                "| Ranked | Hours Coded | Daily Avg |\n"
                "| ------ | ----------- | --------- |\n"
                f"| {data.get('rank', '-')} | "
                f"{data.get('formatted_total_time', '-')} | "
                f"{data.get('daily_avg', '-')} |\n\n"
            )

        top_language = leaderboards.get("top_language", "Unknown")
        tables: List[str] = []
        tables.append("#### Detailed Breakdown\n")
        tables.append(
            build_table("Public Leaderboards (Weekly)", leaderboards.get("global", {}))
        )
        tables.append(
            build_table(
                f"Top Language ({top_language})", leaderboards.get("language", {})
            )
        )
        return "".join(tables)

    def generate_readme_section(
        self, badge_paths: Dict[str, str], leaderboards: Dict[str, Any]
    ) -> str:
        """Combine badge and table sections into markdown"""
        sections: List[str] = []
        if self.config.use_badges:
            sections.append(self.generate_badge_section(badge_paths))
        if self.config.use_tables:
            sections.append(self.generate_table_section(leaderboards))
        return "\n".join(sections)
