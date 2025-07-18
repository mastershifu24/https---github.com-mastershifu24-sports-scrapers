import cloudscraper
from bs4 import BeautifulSoup, Comment
import pandas as pd
from io import StringIO

url = "https://www.basketball-reference.com/boxscores/202506220OKC.html"

#Add headers to mimic a real browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1', 
}

#Fetch the page with headers
scraper = cloudscraper.create_scraper()
res = scraper.get(url, headers=headers)
print(f"Response status: {res.status_code}")
print(f"Content length: {len(res.content)} characters")

soup = BeautifulSoup(res.content, "html.parser")

#Check if the page loaded properly
title = soup.find('title')
print(f"Page title: {title.get_text() if title else 'No title found'}")

#Get all tables (batting tables have class "table_wrapper")
tables = soup.find_all('div', class_='table_wrapper')
print(f"Found {len(tables)} table_wrapper divs")

#Filter to just basketball box score tables
box_tables = []
for table in tables:
    table_id = table.get('id', '')
    print(f"Table ID: {table_id}")
    if 'box-' in table_id.lower() and 'game-basic' in table_id.lower():
        box_tables.append(table)

print(f"Found {len(box_tables)} basketball box score tables")

#Extract tables from HTML comments if not found directly

def extract_table_from_comments(div):
    #Look for HTML comments inside the div
    comments = div.find_all(string=lambda text: isinstance(text, Comment))
    for comment in comments:
        comment_soup = BeautifulSoup(comment, 'html.parser')
        table = comment_soup.find('table')
        if table:
            return table
        return None
    

dfs = []
for i, table_div in enumerate(box_tables):
    #Try to find a table directly
    html_table = table_div.find('table')
    if not html_table:
        #try to extract from comments
        html_table = extract_table_from_comments(table_div)
        if html_table:
            print(f"Extracted table from HTML comment in div {i+1}")
    if html_table:
        try:
            df = pd.read_html(StringIO(str(html_table)))[0]
            team_name = table_div.get('id', f'team_{i}').replace('div_', '')
            df['Team'] = team_name
            dfs.append(df)
            print(f"Successfully processed table {i+1}: {team_name}")
        except Exception as e:
            print(f"Error processing table {i+1}: {e}")
    else:
        print(f"No table found in div {i+1}, even after checking comments.")


print(f"Successfully created {len(dfs)} dataframes")

#Check if we have data to concatenate
if dfs:
    #Combine and clean
    boxscore_df = pd.concat(dfs, ignore_index=True)
    boxscore_df.to_csv('nba_boxscore.csv', index=False)
    print("Box score exported to nba_boxscore.csv")
    print(f"DataFrame shape: {boxscore_df.shape}")
else:
    print("No data to export. Let's inspect the page structure...")
    #Let's see what tables are actually available
    all_tables = soup.find_all('table')
    print(f"Total tables found: {len(all_tables)}")
    for i, table in enumerate(all_tables[:5]): #Show first 5 tables
        print(f"Table {i+1} classes: {table.get('class', 'No class')}")
        print(f"Table {i+1} ID: {table.get('id', 'No ID')}")
        #Show first few rows to understand structure
        rows = table.find_all('tr')[:3]
        if rows:
            print(f"Table {i+1} first row headers: {[th.get_text(strip=True) for th in rows[0].find_all(['th', 'td'])]}")