import pandas as pd
import random

# Function to update duplicate SKU values
def update_duplicates(df):
    # Find duplicates based on 'SKU' column
    duplicates = df[df.duplicated(subset=['SKU'], keep=False)]
    
    # Update duplicates
    for index, row in duplicates.iterrows():
        # Generate a random 2-digit number
        random_number = random.randint(10, 99)
        # Update the SKU value by appending the random number
        df.at[index, 'SKU'] = f"{row['SKU']}-{random_number}"
    
    return df

# Prompt user for input file path
input_file = input("Enter the path to the input CSV file: ")

# Prompt user for output file path
output_file = input("Enter the path for the generated output CSV file: ")

# Load the CSV file into a DataFrame
df = pd.read_csv(input_file)

# Update duplicates
df = update_duplicates(df)

# Save the modified DataFrame back to a CSV file
df.to_csv(output_file, index=False)

print("Duplicate SKU values updated successfully.")
