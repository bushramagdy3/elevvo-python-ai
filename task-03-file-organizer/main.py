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
        sys.exit()

    try:
        addToSubfolders(files_dict, target_directory)
    except Exception as e:
            print("An unexpected error occured while writing the files, please try again")
            print(f"Error: {e}")
            sys.exit()

def directoryToDict(target_directory :str):
    '''Takes a directory and returns a dictionary with files organized based on extentsion'''

    print("Reading directory...")

    try:
        files = os.listdir(target_directory)
    except FileNotFoundError:
        print("Directory not found, please enter a valid one")
        sys.exit()
    
    organized_files = dict()

    for file in files:
        extension = file.split('.')[1]
        
        content = ''
        with open(f"{target_directory}//{file}", "r") as x:
            content = x.read()

        os.remove(f"{target_directory}//{file}")

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
        if extension not in os.listdir(target_directory):
            os.makedirs(extension)

        os.chdir(f"{target_directory}//{extension}")

        for file in files_dict[extension]:
            i = 1
            tmp_file_name = ""
            file_name = file["name"]
            while file_name in os.listdir():
                tmp_file_name = file_name + f"({i})"
                i += 1
            with open(f"{os.curdir()}/{tmp_file_name or file_name}", "w") as new_file:
                new_file.write(file["content"])


if __name__ == "__main__":
    print("Welcome to Bushra's automated file organizer!")
    print("Please enter the path of the directory you'd like to organize:")

    target_directory = input()

    print("Organization Successful!")
