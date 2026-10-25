"""Implementation placeholder for Task 3: Automated File Organizer."""
import os
import sys

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

        extension = file.split('.')[1]
        
        content = ''
        with open(f"{target_directory}\\{file}", "r", encoding='latin-1') as x:
            content = x.read()

        os.remove(f"{target_directory}\\{file}")

        file_name_and_content = dict()
        file_name_and_content["name"] = file
        file_name_and_content["content"] = content

        if extension in organized_files.keys():
            organized_files[extension].append(file_name_and_content)
        else:
            organized_files[extension] = list()
            organized_files[extension].append(file_name_and_content)
    
    return organized_files

def addToSubfolders(files_dict :dict, target_directory :str):
    '''adds dictionary items to subfolders in target_directory'''
    os.chdir(target_directory)

    for extension in files_dict.keys():
        print(f"Organizing .{extension} files...")
        if extension not in os.listdir(target_directory):
            print(f"Created new folder named {extension}")
            os.makedirs(extension)

        os.chdir(f"{target_directory}\\{extension}")

        for file in files_dict[extension]:
            i = 1
            file_name = file["name"]
            original_file_name = file["name"]
            while file_name in os.listdir():
                print(f"Found an already existing file with the name {file_name}, renaming the new file...")
                file_name = original_file_name + f"({i})"
                i += 1
            with open(f"{os.curdir}\\{file_name}", "w", encoding='latin-1') as new_file:
                print(f"Adding {file_name} to the {extension} directory...")
                new_file.write(file["content"])


if __name__ == "__main__":
    print("Welcome to Bushra's automated file organizer!")
    print("Please enter the path of the directory you'd like to organize:")

    target_directory = "C:\\Users\\bushr\\OneDrive\\Desktop\\testing"

    organizeDirectory(target_directory)

    print("Organization Successful!")
