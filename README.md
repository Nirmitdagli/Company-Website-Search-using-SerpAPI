# Company-Website-Search-using-SerpAPI
## Overview
This project uses **SerpAPI** to search and retrieve websites for a list of companies from an Excel file. The script reads company names from an input Excel file, queries the Google Search API via SerpAPI, and saves the corresponding websites to an output Excel file.

---

## Project Structure
- **Script:** `web_search.py` (provided Python script)
- **Input:** `companies.xlsx` (Excel file containing company names)
- **Output:** `companies_with_websites.xlsx` (Excel file containing company names and their corresponding websites)

---

## Requirements
### Python Packages:
- `pandas`
- `requests`
- `openpyxl` (for Excel file handling)

To install the required packages:
```bash
pip install pandas requests openpyxl
