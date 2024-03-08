import os

def remove_spaces(folder_path):
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file name contains spaces
        if ' ' in filename:
            # Replace spaces with underscores
            new_filename = filename.replace(' ', '')
            # Construct the full path of the file
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed '{filename}' to '{new_filename}'")

# Ask user for the folder path
folder_path = input("Enter the folder path: ")
# Check if the entered path is valid
if os.path.isdir(folder_path):
    remove_spaces(folder_path)
    print("Spaces removed from file names in the folder.")
else:
    print("Invalid folder path. Please provide a valid path.")
