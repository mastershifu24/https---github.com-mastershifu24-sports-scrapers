# nba_downloader.py - NBA Data Downloader

import pandas as pd
import cloudscraper
from bs4 import BeautifulSoup
import os
from datetime import datetime
import time

def get_scraper():
    print("Using cloudscraper for requests...")
    return cloudscraper.create_scraper()

def download_table(url, table_id, filename, year):
    print(f"Requesting URL: {url}")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    }
    scraper = get_scraper()
    try:
        response = scraper.get(url, headers=headers)
        print(f"Response status code: {response.status_code}")
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', id=table_id)
        if not table:
            print(f"❌ Could not find table {table_id} for {year}")
            return None
        df = pd.read_html(str(table))[0]
        df = df[df['Rk'].notna()]
        df = df[df['Rk'] != 'Rk']
        df.to_csv(filename, index=False)
        print(f"✅ Saved to {filename} ({len(df)} records)")
        return df
    except Exception as e:
        print(f"❌ Error downloading {filename}: {e}")
        return None

def download_player_stats(year=2024):
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html"
    return download_table(url, "per_game_stats", f"nba_player_stats_{year}.csv", year)

def download_team_stats(year=2024):
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}.html"
    return download_table(url, "team-stats-base", f"nba_team_stats_{year}.csv", year)

def download_advanced_stats(year=2024):
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}_advanced.html"
    return download_table(url, "advanced_stats", f"nba_advanced_stats_{year}.csv", year)

def download_multiple_years(start_year, end_year):
    print(f"🔄 Downloading NBA stats from {start_year} to {end_year}...")
    for year in range(start_year, end_year + 1):
        print(f"\n--- {year} ---")
        download_player_stats(year)
        download_team_stats(year)
        download_advanced_stats(year)
        if year < end_year:
            print("⏳ Waiting 3 seconds before next year...")
            time.sleep(3)
    print(f"\n🎉 Completed downloading NBA stats for {end_year - start_year + 1} years!")

def main():
    print("🏀 NBA Data Downloader")
    print("=" * 50)
    current_year = 2024
    print("\n1. Downloading current year stats...")
    download_player_stats(current_year)
    download_team_stats(current_year)
    download_advanced_stats(current_year)
    print("\n✨ All downloads completed!")
    print("📁 Check your current directory for CSV files")

if __name__ == "__main__":
    main() 