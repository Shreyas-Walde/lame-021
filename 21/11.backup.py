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


schedule.every().day.at("18:50").do(lambda: copy_folder_to_directory(source_dir, destination_dir))
#                  in line anonymous function rather than using an actual function and passing the place holders


while True:
    schedule.run_pending()
    time.sleep(60)

