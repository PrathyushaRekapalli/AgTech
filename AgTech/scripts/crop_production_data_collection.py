### CROP PRODCUTION INDEX
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch the HTML content of the World bank group page
url = "https://databank.worldbank.org/source/world-development-indicators/Series/AG.PRD.CROP.XD"
response = requests.get(url)
html_content = response.text

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Find the relevant table (the first table with class 'dxgvControl_GridDefaultTheme dxgv' in this case)
table = soup.find('table', {'class': 'dxgvTable_GridDefaultTheme dxgvRBB'})

# Step 4: Extract table headers

# Step 5: Extract table rows
rows = []
for tr in table.find_all('tr')[1:]:  # Skipping the header row
    cells = tr.find_all('td')
    row = [cell.text.strip() for cell in cells]
    if len(row) > 0:  # Ensuring the row is not empty
        rows.append(row)
headers = ['Country','1990','2000','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','empty']
# Step 6: Convert to DataFrame
df_crop_production = pd.DataFrame(rows,columns=headers)
df_crop_production.drop(df_crop_production.columns[-2:], axis=1, inplace=True)
df_crop_production.to_csv("cropproductionindex.csv", index=False)

# Step 7: Display the DataFrame
print(df_crop_production.head())