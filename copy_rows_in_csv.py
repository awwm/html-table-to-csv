import csv

# Function to copy and modify rows
def modify_rows(input_csv, output_csv):
    with open(input_csv, 'r', newline='') as infile, open(output_csv, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            # Write original row
            writer.writerow(row)

            # Create new row with modifications
            new_row = row.copy()
            new_row['Type'] = 'variation'
            new_row['SKU'] = ''
            new_row['Name'] = row['Name']
            new_row['Published'] = row['Published']
            new_row['Visibility in catalog'] = row['Visibility in catalog']
            new_row['Short description'] = ''
            new_row['Description'] = ''
            new_row['Tax status'] = row['Tax status']
            new_row['Tax class'] = 'parent'
            new_row['In stock?'] = 1
            new_row['Allow customer reviews?'] = 0
            new_row['Regular price'] = row['Regular price']
            new_row['Categories'] = ''
            new_row['Images'] = ''
            new_row['Parent'] = row['SKU']
            new_row['Attribute 1 name'] = row['Attribute 1 name']
            new_row['Attribute 1 value(s)'] = ''
            new_row['Attribute 1 visible'] = ''
            new_row['Attribute 1 global'] = 1
            writer.writerow(new_row)

            # Modify original row
            row['Regular price'] = ''  # Clear Regular price
            # writer.writerow(row)

# Prompt user for input file path
input_file = input("Enter the path to the input CSV file: ")

# Prompt user for output file path
output_file = input("Enter the path for the generated output CSV file: ")

# Modify rows
modify_rows(input_file, output_file)

print("CSV file modification complete.")
