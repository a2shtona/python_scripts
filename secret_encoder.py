import requests
import pandas as pd
from bs4 import BeautifulSoup

def fetch_and_parse_google_doc(url):
    # Fetch the Google Doc content
    response = requests.get(url)
    response.raise_for_status()# Ensure we notice bad responses

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'lxml')

    # Find the table in the document
    table = soup.find('table')
    if table is None:
        raise ValueError("No table found in the document content.")

    # Extract rows from the table
    rows = table.find_all('tr')
    data = []
    columns = ['x-coordinate', 'Character', 'y-coordinate']

    # Extract table headers to ensure correct columns
    header_row = rows[0].find_all('td') if rows else []
    if not all(header.text.strip() in columns for header in header_row):
        raise ValueError("Table format is incorrect or missing expected headers.")

    for row in rows[1:]:
        cols = row.find_all('td')
        if len(cols) >= 3:
            x = int(cols[0].text.strip())
            char = cols[1].text.strip()
            y = int(cols[2].text.strip())
            data.append([x, char, y])

    if not data:
        raise ValueError("No valid data found in the document content.")

    # Create DataFrame from the data
    df = pd.DataFrame(data, columns=columns)
    return df

def print_grid(df):
    if df is None:
        print("No data to display.")
        return

    # Extract the data from the DataFrame
    positions = df[['x-coordinate', 'Character', 'y-coordinate']].values.tolist()

    # Find the maximum x and y to determine grid size
    max_x = max(pos[0] for pos in positions)
    max_y = max(pos[2] for pos in positions)

    # Initialize grid with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Place characters in the grid
    for x, char, y in positions:
        grid[y][x] = char

    # Print the grid
    for row in grid:
        print(''.join(row))

def main(url):
    df = fetch_and_parse_google_doc(url)
    print_grid(df)

# Sample usage
google_doc_url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
main(google_doc_url)