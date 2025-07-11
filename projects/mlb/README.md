# MLB Box Score Scraper

This script scrapes a full MLB box score and team lineups from Baseball Reference and saves it as a CSV.

## Features
- Uses `cloudscraper` to bypass basic bot protections
- Extracts batting tables, even if hidden in HTML comments
- Outputs clean `mlb_boxscore.csv`

## How to Run
1. Install dependencies:
pip install -r requirements.txt

2. Run the script:
python mlb_scraper.py

## Output
- `mlb_boxscore.csv`: Combined table of batting stats with team labels.