import requests
import json
import time
import csv
import os

# Set up list of websites to retrieve snapshots for
websites = [
    'https://www.khanacademy.org/',
    'https://www.udacity.com/',
    'https://www.coursera.org/',
    'https://www.edx.org/',
    'https://www.udemy.com/',
    'https://www.skillshare.com/',
    'https://www.codecademy.com/',
    'https://www.futurelearn.com/',
    'https://www.babbel.com/',
    'https://www.rosettastone.com/'
]

# Set up date range for snapshots
start_year = 2021
start_month = 1
end_year = time.localtime().tm_year
end_month = time.localtime().tm_mon

# Open CSV file for writing
filename = os.path.join('YOUR DIRECTORY')
with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['website', 'year', 'month', 'snapshot_url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Loop through all the websites and retrieve snapshots for each month
    for website in websites:
        print(f"Retrieving snapshots for website: {website}")
        for year in range(start_year, end_year + 1):
            if year == end_year:
                months = range(start_month, end_month + 1)
            else:
                months = range(start_month, 13)
            for month in months:
                # Construct URL for the snapshot
                snapshot_url = f'https://archive.org/wayback/available?url={website}&timestamp={year}{month:02d}01000000'

                # Send HTTP request to Wayback Machine API
                response = requests.get(snapshot_url)
                data = json.loads(response.content.decode('utf-8'))

                # Check if any snapshots were found
                if 'archived_snapshots' in data:
                    snapshot = data['archived_snapshots']['closest']
                    if snapshot['available']:
                        print(f"Found snapshot for {website} in {year}-{month:02d}")
                        writer.writerow(
                            {'website': website, 'year': year, 'month': month, 'snapshot_url': snapshot['url']})
                    else:
                        print(f"No snapshots found for {website} in {year}-{month:02d}")
                else:
                    print(f"Error retrieving snapshot URL for {website} in {year}-{month:02d}")
                    print(f"Response content: {response.content}")
