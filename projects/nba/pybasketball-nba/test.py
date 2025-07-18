import pandas as pd
import cloudscraper
from bs4 import BeautifulSoup
import os
from datetime import datetime
import time
from playwright.sync_api import sync_playwright

def get_scraper():
    print("Using cloudscraper for requests...")
    return cloudscraper.create_scraper()

def fetch_with_playwright(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        html = page.content()
        browser.close()
        return html

def download_table(url, table_id, filename, year):
    print(f"Requesting URL: {url}")
    try:
        html = fetch_with_playwright(url)
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', id=table_id)
        if not table:
            print(f"Could not find table {table_id} for {year}")
            return None
        df = pd.read_html(str(table))[0]
        df = df[df['Rk'].notna()]
        df = df[df['Rk'] != 'Rk']
        df.to_csv(filename, index=False)
        print(f"Saved to {filename} ({len(df)} records)")
        return df
    except Exception as e:
        print(f"Error downloading {filename}: {e}")
        return None
    
def download_player_stats(year=None):
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html"
    return download_table(url, "per_game_stats", f"nba_player_stats_{year}.csv", year)


def main():
    print("🏀 NBA Data Downloader")
    print("=" * 50)
    current_year = 2024
    print("\n1. Downloading current year stats...")
    download_player_stats(current_year)
    print("\n✨ All downloads completed!")
    print("📁 Check your current directory for CSV files")
    
if __name__ == "__main__":
    main()