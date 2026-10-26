import os
import sys
from pathlib import Path
import logging

def organizeDirectory(target_directory :str, is_dry_run :bool = False ):
    '''scans a target directory and automatically sorts files into subfolders based on file extension'''
    try:
        files_dict = directoryToDict(target_directory)
    except Exception as e:
        logging.error("Could not scan directory: %s. Error: %s", target_directory, e)
        logging.info("Exiting...")
        sys.exit()

    try:
        addToSubfolders(files_dict, target_directory, is_dry_run)
    except Exception as e:
        logging.error("Could not complete file organization in: %s. Error: %s", target_directory, e)
        logging.info("Exiting...")
        sys.exit()

def directoryToDict(target_directory :str):
    '''Takes a directory and returns a dictionary with files organized based on extentsion'''

    logging.info("Scanning directory: %s", target_directory)

    try:
        files = os.listdir(target_directory)
    except FileNotFoundError:
        logging.error("Directory not found: %s. Check the path and try again.", target_directory)
        logging.info("Exiting...")
        sys.exit()
    
    organized_files = dict()

    for file in files:
        path = Path(f"{target_directory}\\{file}")
        if path.is_dir():
            continue

        logging.info("Found file: %s", file)

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
        logging.info("Organizing files with extension '%s'...", extension)

        flag = False

        if not (Path(target_directory) / extension).exists():
            flag = True
            if is_dry_run:
                logging.info("[DRY RUN] Would create folder: %s", Path(target_directory) / extension)
            else:
                logging.info("Creating folder: %s", Path(target_directory) / extension)
                os.makedirs(extension)
        
        if not flag:
            os.chdir(f"{target_directory}\{extension}")

        for file in files_dict[extension]:
            i = 1
            file_name = file
            while not flag and Path(file_name).exists():
                logging.warning("Filename conflict: '%s' already exists in '%s'. Choosing a new destination name...", file_name, Path(target_directory) / extension)
                file_name = file + f"({i})"
                if is_dry_run:
                    logging.info("[DRY RUN] Would rename %s to %s", file, file_name)
                i += 1
            
            source_file = Path(f"{target_directory}\{file}")
            destination_file = Path(f"{target_directory}\{extension}\{file_name}")
            if is_dry_run:
                logging.info(
                    "[DRY RUN] Would move file: %s | Source: %s | Destination: %s",
                    file, source_file, destination_file,
                )
            else:
                source_file.rename(destination_file)
                logging.info(
                    "Moved file: %s | Source: %s | Destination: %s",
                    file, source_file, destination_file,
                )


if __name__ == "__main__":

    logging.basicConfig(
        level=logging.INFO,
        filename=Path(__file__).resolve().with_name("log.log"),
        filemode='w',
        encoding="utf-8",
    )

    print("Welcome to Bushra's automated file organizer!")
    print("Write the path of your targetted directory")
    target_directory = input()
    print("Turn on Dry-run mode? (Y/N)")
    is_dry_run = input()
    is_dry_run = True if is_dry_run == 'Y' else False

    logging.info("Starting file organization (dry_run=%s).", is_dry_run)

    organizeDirectory(target_directory, is_dry_run )

    logging.info("File organization run completed successfully.")
