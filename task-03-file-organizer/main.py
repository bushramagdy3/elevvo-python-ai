import os
import sys
from pathlib import Path
import logging

def organizeDirectory(target_directory :str, is_dry_run :bool = False ):
    '''scans a target directory and automatically sorts files into subfolders based on file extension'''
    try:
        files_dict = directoryToDict(target_directory)
    except Exception as e:
        print(f"Could not scan directory: {target_directory}")
        print(f"Error: {e}")
        print("Exiting...")
        sys.exit()

    try:
        addToSubfolders(files_dict, target_directory, is_dry_run)
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
            organized_files[extension].append(file)
        else:
            organized_files[extension] = list()
            organized_files[extension].append(file)
    
    return organized_files

def addToSubfolders(files_dict :dict, target_directory :str, is_dry_run :bool = False ):
    '''Adds dictionary items to subfolders in target_directory'''

    for extension in files_dict.keys():
        os.chdir(target_directory)
        print(f"Organizing files with extension '.{extension}'...")
        if not (Path(target_directory) / extension).exists():
            if is_dry_run:
                print(f"Would create folder: {Path(target_directory) / extension}")
            else:
                print(f"Creating folder: {Path(target_directory) / extension}")
                os.makedirs(extension)

        os.chdir(f"{target_directory}\{extension}")
        for file in files_dict[extension]:
            i = 1
            file_name = file
            while Path(file_name).exists():
                print(f"Filename conflict: '{file_name}' already exists in '{Path(target_directory) / extension}'. Choosing a new destination name...")
                file_name = file + f"({i})"
                if is_dry_run:
                    print(f"Would rename {file} to {file_name}")
                i += 1
            
            source_file = Path(f"{target_directory}\{file}")
            destination_file = Path(f"{target_directory}\{extension}\{file_name}")
            if is_dry_run:
                print(
                        f"Would move file: {file}\n"
                        f"  Source: {source_file}\n"
                        f"  Destination: {destination_file}"
                    )
            else:
                source_file.rename(destination_file)
                print(
                    f"Moved file: {file}\n"
                    f"  Source: {source_file}\n"
                    f"  Destination: {destination_file}"
                )


if __name__ == "__main__":

    logging.basicConfigconfig(level = logging.INFO, filename='log.log', filemode='w')

    print("Welcome to Bushra's automated file organizer!")
    print("Write the path of your targetted directory")
    target_directory = input()
    print("Turn on Dry-run mode? (Y/N)")
    is_dry_run = input()
    is_dry_run = True if is_dry_run == 'Y' or 'Yes' else False

    print("Starting...")

    organizeDirectory(target_directory, is_dry_run )

    print("File organization completed successfully.")
