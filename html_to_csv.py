from bs4 import BeautifulSoup
import pandas as pd

def extract_text_from_img_tag(tag):
    """
    Extract the text content of the <img> tag.

    Args:
    tag (BeautifulSoup.Tag): The <img> tag.

    Returns:
    str: The text content of the <img> tag.
    """
    return tag.get('src', '')

def extract_text(cell):
    """
    Extract the text content of the cell.

    Args:
    cell (BeautifulSoup.Tag): The cell tag.

    Returns:
    str: The text content of the cell.
    """
    return cell.get_text().strip().replace('\n', ' ')

def prepend_base_url(img_src, base_url):
    """
    Prepend the base URL to the image source.

    Args:
    img_src (str): The original image source.
    base_url (str): The base URL provided by the user.

    Returns:
    str: The modified image source with the base URL prepended.
    """
    return base_url + img_src

def html_table_to_csv(html_file, csv_file, base_url):
    """
    Convert HTML table to CSV file.

    Args:
    html_file (str): Path to the HTML file.
    csv_file (str): Path to save the CSV file.
    base_url (str): The base URL provided by the user.
    """
    # Parse HTML file
    with open(html_file, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Find the table in the HTML
    table = soup.find('table')

    # Extract table data
    table_data = []
    headers = []
    for row in table.find_all('tr'):
        row_data = []
        for idx, cell in enumerate(row.find_all(['th', 'td'])):
            # Extract text content of <img> tags
            if cell.find('img'):
                img_src = extract_text_from_img_tag(cell.find('img'))
                img_src = prepend_base_url(img_src, base_url)  # Prepend base URL to image source
                row_data.append(img_src)
            else:
                row_data.append(extract_text(cell))
            if len(headers) < idx + 1:
                headers.append(cell.get_text().strip())
        table_data.append(row_data)

    # Convert data to DataFrame
    df = pd.DataFrame(table_data[1:], columns=headers)

    # Merge all image columns into one column separated by commas
    image_columns = [col for col in df.columns if 'Images' in col]
    df['allImages'] = df[image_columns].apply(lambda row: ','.join(filter(None, row)), axis=1)

    # Write DataFrame to CSV
    df.to_csv(csv_file, index=False)

def main():
    # Input HTML file path
    html_file = input("Enter the path to the HTML file: ")

    # Output CSV file path
    csv_file = input("Enter the full path to save the CSV file (including filename): ")

    # Input base URL
    base_url = input("Enter the base URL for image sources: ")

    # Convert HTML table to CSV
    html_table_to_csv(html_file, csv_file, base_url)
    print("Conversion completed successfully!")

if __name__ == "__main__":
    main()
