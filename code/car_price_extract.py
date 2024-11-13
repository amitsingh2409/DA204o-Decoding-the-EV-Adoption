import requests
import csv
import time

API_KEY = 'your_api_key'  # Replace with your actual API key
BASE_URL = 'https://api.edmunds.com/api/vehicle/v2/'

def get_msrp(make, model, year):
    """
    Function to get MSRP from API based on car make, model, and year.
    """
    url = f"{BASE_URL}{make}/{model}/{year}/msrp"
    params = {
        'api_key': API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Check for errors or missing data
    if response.status_code == 200 and 'price' in data:
        return data['price']['baseMSRP']
    else:
        print(f"Failed to fetch MSRP for {year} {make} {model}")
        return None

def append_msrp_to_file(input_file, output_file):
    """
    Reads car details from the input file, fetches MSRP, and writes to the output file.
    """
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            year, make, model = row[0].split(' ', 2)
            msrp = get_msrp(make, model, year)
            if msrp:
                row.append(f"${msrp}")
            else:
                row.append("N/A")

            writer.writerow(row)
            time.sleep(1)  # To respect API rate limits

input_file = 'car_list.txt'  # Replace with your file path
output_file = 'car_list_with_msrp.csv'  # Replace with desired output path

append_msrp_to_file(input_file, output_file)
