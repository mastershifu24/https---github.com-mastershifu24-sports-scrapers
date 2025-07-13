# MLB Data Downloader

A Python script to download MLB statistics using the `pybaseball` library. This is a free alternative to Stathead that doesn't require any login credentials or payment.

## Features

- Download batting statistics for any year
- Download pitching statistics for any year  
- Download team batting and pitching statistics
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
   python download_logs.py
   ```

## What it downloads

The script will create CSV files with:
- `batting_stats_YYYY.csv` - Individual player batting statistics
- `pitching_stats_YYYY.csv` - Individual pitcher statistics  
- `team_batting_YYYY.csv` - Team batting statistics
- `team_pitching_YYYY.csv` - Team pitching statistics

## Customization

You can modify the `main()` function in `download_logs.py` to:
- Download different years
- Set qualification thresholds
- Download multiple years at once
- Choose which types of stats to download

## Example usage

```python
# Download current year stats
download_batting_stats(2024)
download_pitching_stats(2024)

# Download multiple years
download_multiple_years(2020, 2024)

# Download with qualification threshold (e.g., 100 plate appearances)
download_batting_stats(2024, qual=100)
```

## Data Sources

This script uses the `pybaseball` library which pulls data from:
- Baseball-Reference.com
- FanGraphs.com
- Other public MLB data sources

## Notes

- No `.env` file needed - this is completely free and doesn't require authentication
- The script includes delays between requests to be respectful to data sources
- All data is saved as CSV files in the current directory 