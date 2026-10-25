"""Implementation placeholder for Task 3: Automated File Organizer."""
import os

def organizeDirectory(target_directory :str):
    '''scans a target directory and automatically sorts files into subfolders based on file extension'''
    directoryToDict(target_directory)

def directoryToDict(target_directory :str):
    '''Takes a directory and returns a dictionary with files organized based on extentsion'''

    files = os.listdir(target_directory)
    
    organized_files = dict()

    for file in files:
        extension = file.split('.')[1]

        if extension in organized_files.keys():
            organized_files[extension].append(file)
        else:
            organized_files[extension] = list()
            organized_files[extension].append(file)
    
    return organized_files


if __name__ == "__main__":
    print("Welcome to Bushra's automated file organizer!")
    print("Please enter the path of the directory you'd like to organize:")

    target_directory = input()

    print(organizeDirectory(target_directory))
