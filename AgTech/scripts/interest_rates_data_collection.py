### Fetching interest rates
import requests
from bs4 import BeautifulSoup
import pandas as pd


# Step 1: Fetch the HTML content of the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_sovereign_states_by_central_bank_interest_rates"
response = requests.get(url)
html_content = response.text

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Find the relevant table (the first table with class 'wikitable' in this case)
table = soup.find('table', {'class': 'wikitable'})

# Step 4: Extract table headers
headers = []
for th in table.find_all('th'):
    headers.append(th.text.strip())

# Step 5: Extract table rows
rows = []
for tr in table.find_all('tr')[1:]:  # Skipping the header row
    cells = tr.find_all('td')
    row = [cell.text.strip() for cell in cells]
    if len(row) > 0:  # Ensuring the row is not empty
        rows.append(row)

# Step 6: Convert to DataFrame
df_interest = pd.DataFrame(rows, columns=headers)
df_interest = df_interest.rename(columns={'Country orcurrency union': 'Country'})
df_interest.to_csv("interestrate.csv", index=False)

# Step 7: Display the DataFrame
print(df_interest.head())