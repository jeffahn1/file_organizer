import os
import shutil

# Replace this with the path to the directory you want to organize
directory = '/Users/jeffreyjahn/Downloads'

# Dictionary for file extensions and folder names
file_extensions = {
    'pdf': 'PDFs',
    'png': 'Images',
    'jpg': 'Images',
    'jpeg': 'Images',
    'gif': 'Images',
    'doc': 'Documents',
    'docx': 'Documents',
    'txt': 'Documents',
    'csv': 'Data',
    'xlsx': 'Data',
    'zip': 'Archives',
    'rar': 'Archives',
    'mp3': 'Music',
    'wav': 'Music',
    'mp4': 'Videos',
    'avi': 'Videos',
    'flv': 'Videos',
    'wmv': 'Videos',
    # Add more file types as needed
}

# Go through each file in the directory
for filename in os.listdir(directory):
    if not os.path.isfile(os.path.join(directory, filename)):
        continue

    # Get file extension
    ext = filename.split('.')[-1].lower()

    # Check if the extension is in the dictionary
    if ext in file_extensions:
        folder_name = file_extensions[ext]
        folder_path = os.path.join(directory, folder_name)

        # Create a folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Move the file
        shutil.move(os.path.join(directory, filename), folder_path)

print("Files have been organized.")
