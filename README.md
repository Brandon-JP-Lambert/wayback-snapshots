# Wayback-Snapshots

This Python script retrieves snapshots of specified websites from the Wayback Machine and saves the snapshot URLs in a CSV file. The Wayback Machine is a digital archive of the World Wide Web, providing access to historical versions of webpages.

## Features

- Retrieve snapshots for a list of websites
- Specify a date range for snapshots
- Save snapshot URLs in a CSV file

## Usage

1. Clone or download the repository.
2. Install the required packages.
3. Open the script in your favorite code editor.
4. Modify the `websites` list to include the websites you want to retrieve snapshots for.
5. Set the `start_year`, `start_month`, `end_year`, and `end_month` variables to the desired date range.
6. Update the `filename` variable with the path to the desired location for the output CSV file.
7. Run the script using `python wayback_snapshot_downloader.py` (or the name you saved the script as).

## Output

Here's an example of the script's Python output when retrieving snapshots for popular online learning platforms:

```
Retrieving snapshots for website: https://www.khanacademy.org/
Found snapshot for https://www.khanacademy.org/ in 2021-01
No snapshots found for https://www.khanacademy.org/ in 2021-02
...
```

The script generates a CSV file containing the following columns:

| website                      | year | month | snapshot_url                                     |
|------------------------------|------|-------|--------------------------------------------------|
| https://www.khanacademy.org/ | 2021 | 1     | http://web.archive.org/web/20210109021835/...    |
| https://www.khanacademy.org/ | 2021 | 3     | http://web.archive.org/web/20210317015535/...    |
| https://www.khanacademy.org/ | 2021 | 4     | http://web.archive.org/web/20210409174855/...    |
| https://www.udacity.com/     | 2021 | 1     | http://web.archive.org/web/20210110020409/...    |
| https://www.udacity.com/     | 2021 | 2     | http://web.archive.org/web/20210209044423/...    |
| ...                          | ...  | ...   | ...                                              |

## Limitations

The script uses the Wayback Machine API, which may have limitations in terms of rate limits or availability. In some cases, there might be no snapshots available for a specific website and month.

## Reference:
The Wayback Machine's API documentation can be found at: https://archive.org/help/wayback_api.php
