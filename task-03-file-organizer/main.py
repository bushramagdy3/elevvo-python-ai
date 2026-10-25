import os
import sys
from pathlib import Path

def organizeDirectory(target_directory :str):
    '''scans a target directory and automatically sorts files into subfolders based on file extension'''
    try:
        files_dict = directoryToDict(target_directory)
    except Exception as e:
        print(f"Could not scan directory: {target_directory}")
        print(f"Error: {e}")
        print("Exiting...")
        sys.exit()

    try:
        addToSubfolders(files_dict, target_directory)
    except Exception as e:
            print(f"Could not complete file organization in: {target_directory}")
            print(f"Error: {e}")
            print("Exiting...")
            sys.exit()

def directoryToDict(target_directory :str):
    '''Takes a directory and returns a dictionary with files organized based on extentsion'''

    print(f"Scanning directory: {target_directory}")

    try:
        files = os.listdir(target_directory)
    except FileNotFoundError:
        print(f"Directory not found: {target_directory}. Check the path and try again.")
        print("Exiting...")
        sys.exit()
    
    organized_files = dict()

    for file in files:
        path = Path(f"{target_directory}\\{file}")
        if path.is_dir():
            continue

        print(f"Found file: {file}")

        extension = path.suffix.lower()
        if not extension:
            extension = "Others"

        if extension in organized_files.keys():
            organized_files[extension].append(file.lower())
        else:
            organized_files[extension] = list()
            organized_files[extension].append(file.lower())
    
    return organized_files

def addToSubfolders(files_dict :dict, target_directory :str):
    '''Adds dictionary items to subfolders in target_directory'''

    for extension in files_dict.keys():
        os.chdir(target_directory)
        print(f"Organizing files with extension '.{extension}'...")
        if extension not in os.listdir(target_directory):
            print(f"Creating folder: {Path(target_directory) / extension}")
            os.makedirs(extension)

        os.chdir(f"{target_directory}\{extension}")
        for file in files_dict[extension]:
            i = 1
            file_name = file
            while file_name in (x.lower() for x in os.listdir()):
                print(f"Filename conflict: '{file_name}' already exists in '{Path(target_directory) / extension}'. Choosing a new destination name...")
                file_name = file + f"({i})"
                i += 1
            source_file = Path(f"{target_directory}\{file}")
            destination_file = Path(f"{target_directory}\{extension}\{file_name}")
            source_file.rename(destination_file)
            print(
                f"Moved file: {file}\n"
                f"  Source: {source_file}\n"
                f"  Destination: {destination_file}"
            )


if __name__ == "__main__":
    print("Welcome to Bushra's automated file organizer!")
    print("Starting file organization...")

    target_directory = "C:\\Users\\bushr\\OneDrive\\Desktop\\testing"

    organizeDirectory(target_directory)

    print("File organization completed successfully.")
