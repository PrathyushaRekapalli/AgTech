## Fetching GDP country wise
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch the HTML content of the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
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

# **IMP** This is something we need to take care manully for each table
headers = ['Country','IMF_Estimate','IMF_Year','WB_Estimate','WB_Year','UN_Estimate','UN_Year']

# Step 6: Convert to DataFrame
df_gdp = pd.DataFrame(rows, columns=headers)
df_gdp.to_csv("gdp.csv", index=False)
# Step 7: Display the DataFrame
df_gdp= df_gdp.sort_values(by='Country')
print(df_gdp.head())

### Fetching interest rates

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

import re
# Removing annotations from estimates
df_gdp['IMF_Estimate'] = df_gdp['IMF_Estimate'].astype(str).apply(lambda x: re.sub(r'\[.*\]', '', x))
df_gdp['WB_Estimate'] = df_gdp['WB_Estimate'].astype(str).apply(lambda x: re.sub(r'\[.*\]', '', x))
df_gdp['UN_Estimate'] = df_gdp['UN_Estimate'].astype(str).apply(lambda x: re.sub(r'\[.*\]', '', x))

df_gdp['IMF_Estimate'] = pd.to_numeric(df_gdp['IMF_Estimate'].str.replace(',', ''), errors='coerce')
df_gdp['WB_Estimate'] = pd.to_numeric(df_gdp['WB_Estimate'].str.replace(',', ''), errors='coerce')
df_gdp['UN_Estimate'] = pd.to_numeric(df_gdp['UN_Estimate'].str.replace(',', ''), errors='coerce')

import pandas as pd
import matplotlib.pyplot as plt

# Step 0: Clean and convert the crop production index data to numeric
for col in df_crop_production.columns[1:]:  # Exclude 'Country' column
    df_crop_production[col] = pd.to_numeric(df_crop_production[col], errors='coerce')
# Step 1: Calculate average crop production index
df_crop_production['Average_Crop_Index'] = df_crop_production.iloc[:, 1:].mean(axis=1)

# Step 2: Select top countries by average crop production index
top_n = 10  # Adjust as needed
top_countries_crop = df_crop_production.sort_values(by='Average_Crop_Index', ascending=False).head(top_n)['Country']

# Step 3: Filter GDP data for selected countries
df_gdp_selected = df_gdp[df_gdp['Country'].isin(top_countries_crop)]
# Step 4: Filter interest data for selected countries
df_interest_selected = df_interest[df_interest['Country'].isin(top_countries_crop)]
# Step 5: Filter crop production data for selected countries
df_crop_production_selected = df_crop_production[df_crop_production['Country'].isin(top_countries_crop)]

df_gdp_selected

df_crop_production_selected.drop(df_crop_production_selected.index[-1])

# Plotting GDP estimates
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))

# Bar plot for GDP estimates
ax1.bar(df_gdp_selected['Country'], df_gdp_selected['IMF_Estimate'], label='IMF Estimate', alpha=0.7)
ax1.bar(df_gdp_selected['Country'], df_gdp_selected['WB_Estimate'], bottom=df_gdp_selected['IMF_Estimate'], label='WB Estimate', alpha=0.7)
ax1.bar(df_gdp_selected['Country'], df_gdp_selected['UN_Estimate'], bottom=df_gdp_selected['IMF_Estimate'] + df_gdp_selected['WB_Estimate'], label='UN Estimate', alpha=0.7)

# Plotting crop production index
for country in df_crop_production_selected['Country']:
    ax2.plot(df_crop_production_selected.columns[1:-1], df_crop_production_selected[df_crop_production_selected['Country'] == country].values.flatten()[1:-1], marker='o', label=country)

# Set labels and title for GDP plot
ax1.set_xlabel('Country')
ax1.set_ylabel('GDP Estimate')
ax1.set_title('Comparison of GDP Estimates')
ax1.legend()

# Set labels and title for crop production plot
ax2.set_xlabel('Year')
ax2.set_ylabel('Crop Production Index')
ax2.set_title('Crop Production Index Comparison')
ax2.legend()

# Rotate x-axis labels for better visibility in GDP plot
plt.setp(ax1.get_xticklabels(), rotation=45)

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()

#Bar Plot for Average Crop Index
# Plotting
plt.figure(figsize=(10, 6))
plt.bar(df_crop_production_selected['Country'], df_crop_production_selected['Average_Crop_Index'])
plt.xlabel('Country')
plt.ylabel('Average Crop Index')
plt.title('Average Crop Index Across Countries')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#Line Plot for Central Bank Interest Rates
# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df_interest_selected['Country'], df_interest_selected['Central bankinterest rate (%)'], marker='o', label='Interest Rate')
plt.plot(df_interest_selected['Country'], df_interest_selected['Average inflation rate2017–2021 (%)by WB and IMF[1][2]as in the List'], marker='x', label='Average Inflation Rate')
plt.xlabel('Country')
plt.ylabel('Rates (%)')
plt.title('Central Bank Interest Rates vs Average Inflation Rate')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()

#Scatter Plot for GDP Estimates
# Plotting
plt.figure(figsize=(12, 8))
bar_width = 3.0
index = df_gdp_selected.index

plt.bar(index - bar_width, df_gdp_selected['IMF_Estimate'], width=bar_width, label='IMF Estimate')
plt.bar(index, df_gdp_selected['WB_Estimate'], width=bar_width, label='WB Estimate')
plt.bar(index + bar_width, df_gdp_selected['UN_Estimate'], width=bar_width, label='UN Estimate')

plt.xlabel('Country')
plt.ylabel('GDP Estimate')
plt.title('Comparison of GDP Estimates by Organization')
plt.xticks(index, df_gdp_selected['Country'], rotation=45)
plt.legend()

plt.tight_layout()

plt.show()











