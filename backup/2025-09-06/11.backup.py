import os 
import shutil  # copy operations
import datetime
import schedule
import time

source_dir = "S:/My Stuff/PyCodes/lame-021/21"
destination_dir = "S:/My Stuff/PyCodes/lame-021/backup"


def copy_folder_to_directory(source, dest):
    today = datetime.date.today()  # gets today's date
    dest_dir = os.path.join(dest, str(today))
    # joining today date to path    


    try:
        shutil.copytree(source,dest_dir) # copies everything recursively
        print(f"Folder copied to: {dest_dir}")

    except FileExistsError:
        print(f"Folder already exists in: {dest}")

copy_folder_to_directory(source_dir, destination_dir)