import os
import sys
from pathlib import Path

def organizeDirectory(target_directory :str):
    '''scans a target directory and automatically sorts files into subfolders based on file extension'''
    try:
        files_dict = directoryToDict(target_directory)
    except Exception as e:
        print("An unexpected error occured while reading the files, please try again")
        print(f"Error: {e}")
        print("Exiting...")
        sys.exit()

    try:
        addToSubfolders(files_dict, target_directory)
    except Exception as e:
            print("An unexpected error occured while writing the files, please try again")
            print(f"Error: {e}")
            print("Exiting...")
            sys.exit()

def directoryToDict(target_directory :str):
    '''Takes a directory and returns a dictionary with files organized based on extentsion'''

    print("Reading directory...")

    try:
        files = os.listdir(target_directory)
    except FileNotFoundError:
        print("Directory not found, please enter a valid one")
        print("Exiting...")
        sys.exit()
    
    organized_files = dict()

    for file in files:
        if '.' not in file:
            continue

        print(f"Reading file {file}")

        extension = file.split('.')[-1]

        if extension in organized_files.keys():
            organized_files[extension].append(file)
        else:
            organized_files[extension] = list()
            organized_files[extension].append(file)
    
    return organized_files

def addToSubfolders(files_dict :dict, target_directory :str):
    '''Adds dictionary items to subfolders in target_directory'''

    for extension in files_dict.keys():
        os.chdir(target_directory)
        print(f"Organizing .{extension} files...")
        if extension not in os.listdir(target_directory):
            print(f"Created new folder named {extension}")
            os.makedirs(extension)

        os.chdir(f"{target_directory}\{extension}")
        for file in files_dict[extension]:
            i = 1
            file_name = file
            while file_name in os.listdir():
                print(f"Found an already existing file with the name {file_name}, renaming the new file...")
                file_name = file + f"({i})"
                i += 1
            source_file = Path(f"{target_directory}\{file}")
            destination_file = Path(f"{target_directory}\{extension}\{file_name}")
            source_file.rename(destination_file)


if __name__ == "__main__":
    print("Welcome to Bushra's automated file organizer!")
    print("Please enter the path of the directory you'd like to organize:")

    target_directory = "C:\\Users\\bushr\\OneDrive\\Desktop\\testing"

    organizeDirectory(target_directory)

    print("Organization Successful!")
