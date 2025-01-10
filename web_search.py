import pandas as pd
import requests
import time

# Replace with your SerpAPI key
SERP_API_KEY = "04b6b6be4aea66ecd156265820448b79e4accbb39a5cc225c75eb4f384f7a742"

# Function to get website from company name
def get_website(company_name):
    url = "https://serpapi.com/search"
    params = {
        "q": company_name,
        "api_key": SERP_API_KEY,
        "engine": "google",
        "location": "United States"
    }
    try:
        print(f"Fetching website for: {company_name}")
        response = requests.get(url, params=params, timeout=10)  # Add a timeout
        response.raise_for_status()  # Raises an HTTPError if the response code is not 200
        results = response.json()
        time.sleep(2)  # Add a delay of 2 seconds between requests to avoid rate limiting
        if 'organic_results' in results and len(results['organic_results']) > 0:
            return results['organic_results'][0].get('link', "Not Found")
        else:
            return "Not Found"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website for {company_name}: {e}")
        return "Not Found"

# Load companies from Excel file
def load_companies(file_path):
    try:
        df = pd.read_excel(file_path)
        if 'Company' not in df.columns:
            raise ValueError("Input Excel file must have a 'Company' column.")
        return df
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return pd.DataFrame()
    except ValueError as ve:
        print(f"Error: {ve}")
        return pd.DataFrame()

# Write results back to Excel
def save_websites(df, file_path):
    if not df.empty:
        df.to_excel(file_path, index=False)
    else:
        print("No data to save.")

# Main function
def main(input_file, output_file):
    df = load_companies(input_file)
    if not df.empty:
        df['Website'] = df['Company'].apply(get_website)
        save_websites(df, output_file)
        print(f"Websites saved to {output_file}")
    else:
        print("No companies to process.")

if __name__ == "__main__":
    input_excel = "companies.xlsx"  # Excel file with list of companies
    output_excel = "companies_with_websites.xlsx"  # Output Excel file with websites
    main(input_excel, output_excel)
