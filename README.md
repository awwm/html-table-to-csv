# HTML Table to CSV Converter

This Python script converts an HTML table into a CSV file. It extracts data from the HTML table, including image sources, and writes the data into a CSV file. It also allows the user to specify a base URL for image sources.

## Features

- Extracts data from HTML tables.
- Handles image sources in HTML tables.
- Allows customization of the base URL for image sources.

## How to Use

### Clone
- git clone https://github.com/awwm/html-table-to-csv.git

### Prerequisites

Before running the script, ensure you have the following installed:

- Python (version 3.6 or higher)
- BeautifulSoup library (`bs4`)
- pandas library (`pandas`)

You can install the required libraries using pip:

```bash
pip install beautifulsoup4 pandas
```

### Run the script
- python html_to_csv.py

# Remove Spaces from File Names

This Python script removes spaces from file names within a specified folder by replacing them with underscores.

### Run the script
- python remove_spaces_from_file_names.py