# NBA Data Downloader

A Python script to download NBA statistics from Basketball-Reference.com. This is a free alternative that doesn't require any login credentials or payment.

## Features

- Download NBA player statistics for any year
- Download NBA team statistics for any year
- Download NBA advanced statistics for any year
- Download multiple years at once
- Save data as CSV files
- No login required - completely free!

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the script:**
   ```bash
   python nba_downloader.py
   ```

## What it downloads

The script will create CSV files with:
- `nba_player_stats_YYYY.csv` - Individual player statistics (per game)
- `nba_team_stats_YYYY.csv` - Team statistics
- `nba_advanced_stats_YYYY.csv` - Advanced player statistics (PER, VORP, etc.)

## Customization

You can modify the `main()` function in `nba_downloader.py` to:
- Download different years
- Download multiple years at once
- Choose which types of stats to download

## Example usage

```python
# Download current year stats
download_player_stats(2024)
download_team_stats(2024)
download_advanced_stats(2024)

# Download multiple years
download_multiple_years(2020, 2024)
```

## Data Sources

This script pulls data from:
- Basketball-Reference.com (per game stats)
- Basketball-Reference.com (team stats)
- Basketball-Reference.com (advanced stats)

## Notes

- No `.env` file needed - this is completely free and doesn't require authentication
- The script includes delays between requests to be respectful to data sources
- All data is saved as CSV files in the current directory
- Uses proper headers to avoid being blocked by the website 