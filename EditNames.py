import os

def rename_files(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            # Remove the first two characters from the file name
            new_filename = filename[0:]   #Borra la cantidad de caracteres que definimos de izquierda a derecha
            new_file_path = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(os.path.join(folder_path, filename), new_file_path)

            print(f"Renamed: {filename} to {new_filename}")


# Specify the absolute folder path containing your files
folder_path = r'C:\Users\franc\Documents\Sidify Music Converter\L&F&J'

# Call the function to change the names
rename_files(folder_path)
