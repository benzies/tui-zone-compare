import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

import tomli 
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.style import Style

def get_timezones() -> list[str]:
    """Reads timezone configuration from a file."""
    # Get the directory where the script is located
    script_dir = Path(__file__).resolve().parent
    # Define the path to the config file
    config_path = script_dir / "config.toml"

    # Default timezones to use if the config file is not found
    default_zones = ["UTC", "America/New_York", "Europe/London", "Australia/Sydney"]

    if not config_path.is_file():
        print(f"Info: Config file not found at {config_path}. Using default timezones.", file=sys.stderr)
        return default_zones

    try:
        with open(config_path, "rb") as f:
            config_data = tomli.load(f)

        zones = config_data.get("timezones", [])
        if not zones:
            print("Warning: 'timezones' key is missing or empty in config. Using defaults.", file=sys.stderr)
            return default_zones

        # Validate that the timezones exist
        valid_zones = []
        for tz_name in zones:
            try:
                ZoneInfo(tz_name)
                valid_zones.append(tz_name)
            except ZoneInfoNotFoundError:
                print(f"Warning: Timezone '{tz_name}' from config not found. Skipping.", file=sys.stderr)
        return valid_zones

    except tomli.TOMLDecodeError:
        print(f"Error: Could not parse {config_path}. Please check its format. Using defaults.", file=sys.stderr)
        return default_zones

def generate_table(timezones: list[str]) -> Table:
    """Generates and returns the rich Table object for the current time."""
    now_utc = datetime.now(ZoneInfo("UTC"))
    table = Table(title="🌎 Timezone Comparison", border_style="blue")

    for tz_name in timezones:
        offset_seconds = now_utc.astimezone(ZoneInfo(tz_name)).utcoffset().total_seconds()
        offset_hours = offset_seconds / 3600
        offset_str = f"{offset_hours:+0.0f}h"
        table.add_column(f"{tz_name}\n({offset_str})", justify="center", header_style="bold cyan")

    current_hour_style = Style(bgcolor="bright_blue")

    for hour_delta in range(-12, 13):
        row_data = []
        is_current_hour_row = (hour_delta == 0)
        target_time_utc = (now_utc + timedelta(hours=hour_delta)).replace(minute=0, second=0, microsecond=0)

        for tz_name in timezones:
            local_time = target_time_utc.astimezone(ZoneInfo(tz_name))
            row_data.append(local_time.strftime("%a %H:%M"))

        style = current_hour_style if is_current_hour_row else None
        table.add_row(*row_data, style=style)

    return table

def main():
    # Now it gets timezones from the config file automatically
    timezones = get_timezones()
    console = Console()

    try:
        with Live(generate_table(timezones), screen=True, vertical_overflow="visible") as live:
            while True:
                # Refresh every minute to update the table on the hour change
                time.sleep(60)
                live.update(generate_table(timezones))
    except KeyboardInterrupt:
        print("\nExiting.")

if __name__ == "__main__":
    main()
