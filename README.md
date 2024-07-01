# AgTech
Data Collection Tool Documentation

This repository contains Python scripts to collect data from various sources related to GDP estimates, central bank interest rates, and crop production indices.Below are the details for each component:

1. GDP Data Collection:

Script: gdp_data_collection.py
Description: This script fetches GDP data from the Wikipedia page on nominal GDP.
Setup: Ensure Python dependencies (requests, beautifulsoup4, pandas) are installed.
Execution: Run the script to fetch data and generate gdp.csv.
Example Output: The resulting CSV file contains GDP estimates from various organizations for different countries.

2. Interest Rate Data Collection:
Script: interest_rate_data_collection.py
Description: This script retrieves central bank interest rate data from a Wikipedia page.
Setup: Dependencies required: requests, beautifulsoup4, pandas.
Execution: Execute the script to fetch data and save it as interestrate.csv.
Example Output: The generated CSV file includes interest rates for sovereign states and currency unions.

3. Crop Production Index Data Collection:
Script: crop_production_data_collection.py
Description: This script scrapes crop production index data from the World Bank Data Bank.
Setup: Dependencies needed: requests, beautifulsoup4, pandas.
Execution: Run the script to collect data and export it as cropproductionindex.csv.
Example Output: The resulting CSV file contains yearly crop production indices for various countries.

2. Setup Instructions:

1.Clone the repository:
https://github.com/PrathyushaRekapalli/AgTech
cd AgTech
2. Install dependencies:
pip install -r requirements.txt
3.Execute each script to fetch data:
python scripts/gdp_data_collection.py
python scripts/interest_rate_data_collection.py
python scripts/crop_production_data_collection.py
4.View the generated CSV files in the root directory:
gdp.csv: GDP estimates
interestrate.csv: Interest rates
cropproductionindex.csv: Crop production indices
Contact:
For any questions or issues, please contact rekapalliprathyusha21@gmail.com.

