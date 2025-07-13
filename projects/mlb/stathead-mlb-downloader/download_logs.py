# download_logs.py - MLB Data Downloader using pybaseball

import pandas as pd
from pybaseball import batting_stats, pitching_stats, team_batting, team_pitching
import os
from datetime import datetime
import time

def download_batting_stats(year=None, qual=0):
    """
    Download batting statistics for a given year.
    
    Args:
        year (int): Year to download stats for (default: current year)
        qual (int): Minimum plate appearances to qualify (default: 0 for all players)
    """
    if year is None:
        year = datetime.now().year
    
    print(f"📊 Downloading batting stats for {year}...")
    
    try:
        # Get batting stats
        batting_data = batting_stats(year, qual=qual)
        
        # Save to CSV
        filename = f"batting_stats_{year}.csv"
        batting_data.to_csv(filename, index=False)
        print(f"✅ Saved batting stats to {filename}")
        print(f"📈 Downloaded {len(batting_data)} player records")
        
        return batting_data
        
    except Exception as e:
        print(f"❌ Error downloading batting stats: {e}")
        return None

def download_pitching_stats(year=None, qual=0):
    """
    Download pitching statistics for a given year.
    
    Args:
        year (int): Year to download stats for (default: current year)
        qual (int): Minimum innings pitched to qualify (default: 0 for all pitchers)
    """
    if year is None:
        year = datetime.now().year
    
    print(f"⚾ Downloading pitching stats for {year}...")
    
    try:
        # Get pitching stats
        pitching_data = pitching_stats(year, qual=qual)
        
        # Save to CSV
        filename = f"pitching_stats_{year}.csv"
        pitching_data.to_csv(filename, index=False)
        print(f"✅ Saved pitching stats to {filename}")
        print(f"📈 Downloaded {len(pitching_data)} pitcher records")
        
        return pitching_data
        
    except Exception as e:
        print(f"❌ Error downloading pitching stats: {e}")
        return None

def download_team_stats(year=None):
    """
    Download team batting and pitching statistics for a given year.
    
    Args:
        year (int): Year to download stats for (default: current year)
    """
    if year is None:
        year = datetime.now().year
    
    print(f"🏟️ Downloading team stats for {year}...")
    
    try:
        # Get team batting stats
        team_batting_data = team_batting(year)
        team_batting_filename = f"team_batting_{year}.csv"
        team_batting_data.to_csv(team_batting_filename, index=False)
        print(f"✅ Saved team batting stats to {team_batting_filename}")
        
        # Get team pitching stats
        team_pitching_data = team_pitching(year)
        team_pitching_filename = f"team_pitching_{year}.csv"
        team_pitching_data.to_csv(team_pitching_filename, index=False)
        print(f"✅ Saved team pitching stats to {team_pitching_filename}")
        
        return team_batting_data, team_pitching_data
        
    except Exception as e:
        print(f"❌ Error downloading team stats: {e}")
        return None, None

def download_multiple_years(start_year, end_year, include_team_stats=True):
    """
    Download stats for multiple years.
    
    Args:
        start_year (int): Starting year
        end_year (int): Ending year
        include_team_stats (bool): Whether to include team stats
    """
    print(f"🔄 Downloading stats from {start_year} to {end_year}...")
    
    for year in range(start_year, end_year + 1):
        print(f"\n--- {year} ---")
        
        # Download player stats
        batting_data = download_batting_stats(year)
        pitching_data = download_pitching_stats(year)
        
        # Download team stats if requested
        if include_team_stats:
            team_batting, team_pitching = download_team_stats(year)
        
        # Add delay to be respectful to the data source
        if year < end_year:
            print("⏳ Waiting 2 seconds before next year...")
            time.sleep(2)
    
    print(f"\n🎉 Completed downloading stats for {end_year - start_year + 1} years!")

def main():
    """
    Main function to run the MLB data downloader.
    """
    print("🚀 MLB Data Downloader using pybaseball")
    print("=" * 50)
    
    # Example usage - you can modify these parameters
    current_year = datetime.now().year
    
    # Download current year stats
    print("\n1. Downloading current year stats...")
    download_batting_stats(current_year)
    download_pitching_stats(current_year)
    download_team_stats(current_year)
    
    # Uncomment the lines below to download multiple years
    # print("\n2. Downloading last 5 years...")
    # download_multiple_years(current_year - 4, current_year)
    
    print("\n✨ All downloads completed!")
    print("📁 Check your current directory for CSV files")

if __name__ == "__main__":
    main()
