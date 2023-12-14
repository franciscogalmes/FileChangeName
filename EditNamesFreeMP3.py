import os
import re


def remove_text_from_filenames(folder_path, text_to_remove):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            # Check if the text to remove is present in the file name (case-insensitive)
            if re.search(re.escape(text_to_remove), filename, flags=re.IGNORECASE):
                # Remove the specified text from the file name
                new_filename = re.sub(re.escape(text_to_remove), '', filename, flags=re.IGNORECASE)
                new_file_path = os.path.join(folder_path, new_filename)

                # Rename the file
                os.rename(os.path.join(folder_path, filename), new_file_path)

                print(f"Renamed: {filename} to {new_filename}")


# Specify the absolute folder path containing your files
folder_path = r'C:\Users\franc\Documents\Sidify Music Converter\L&F&J'

# Specify the text you want to remove from the file names
text_to_remove = '(freemp3)'   #linea completa a remover

# Call the function to remove the specified text from file names
remove_text_from_filenames(folder_path, text_to_remove)
