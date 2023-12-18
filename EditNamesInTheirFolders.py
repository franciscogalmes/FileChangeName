import os
import re

def remove_text_from_filenames(root_folder, phrases_to_remove):
    changed_files_count = 0

    for folder_path, _, filenames in os.walk(root_folder):
        for filename in filenames:
            original_file_path = os.path.join(folder_path, filename)

            print(f"Processing: {original_file_path}")

            for phrase in phrases_to_remove:
                # Check if the text to remove is present in the file name (case-insensitive)
                if re.search(re.escape(phrase), filename, flags=re.IGNORECASE):
                    print(f"Found phrase: {phrase}")

                    # Remove the specified text from the file name
                    new_filename = re.sub(re.escape(phrase), '', filename, flags=re.IGNORECASE)

                    # Construct the new file path
                    new_file_path = os.path.join(folder_path, new_filename)

                    try:
                        # Rename the file
                        os.rename(original_file_path, new_file_path)

                        changed_files_count += 1
                        print(f"Renamed: {original_file_path} to {new_file_path}")
                    except FileNotFoundError as e:
                        print(f"Error: {e}")
                        print(f"Original path: {original_file_path}")
                        print(f"New path: {new_file_path}")

    print(f"\nTotal files changed: {changed_files_count}")

# Specify the absolute folder path containing your files and subfolders
root_folder = r'C:\Users\franc\Desktop\Contents'

# Specify the phrases you want to remove from the file names
phrases_to_remove = ['myfreemp3.vip', 'myfreemp3', r'\[YT2mp3\.info\] - ', r'\(320kbps\)', 'y2mate.com -'   ]

# Call the function to remove the specified phrases from file names in the root folder and its subfolders
remove_text_from_filenames(root_folder, phrases_to_remove)
