import os 
import shutil
from datetime import datetime
import time
import logging

print(f"Script Initalizing...")
time.sleep(3)
print("Script Initalizing.....")
time.sleep(3)
print("Script Initalizing..........")
folder_path = str(input("folder_path?"))



logging.basicConfig(filename="logfile.log",
                    format='%(asctime)s %(levelname)s: %(message)s',
                    filemode= 'a'
)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

archive_path = os.path.join(folder_path, "archive")
path_2024 = os.path.join(archive_path, "2024")
path_2025 = os.path.join(archive_path, "2025")

if not os.path.exists(archive_path):
    os.mkdir(archive_path)
    if not os.path.exists(path_2024):
        os.makedirs(path_2024, exist_ok=True)
        if not os.path.exists(path_2025):
            os.makedirs(path_2025, exist_ok=True)
print("Folders created successfully !!!")

def unique_name(folder_name, file_name ):
    """Rename file if name already exists"""
    base, ext = os.path.splitext(file_name)
    counter = 1
    new_name = file_name

    while os.path.exists(os.path.join(folder_name, new_name)):
        new_name = f"{base}_{counter}{ext}"
        counter += 1

    return new_name


for filename in os.listdir(folder_path):
    filename_path = os.path.join(folder_path, filename)


    if os.path.isfile(filename_path) and filename.endswith((".pdf", ".xlsx")):
        
        try:
         mod_time = os.path.getmtime(filename_path)
         human_time = datetime.fromtimestamp(mod_time)
         now = datetime.now()
         age_days = (now - human_time).days
         if age_days > 90 and human_time.year == 2024:
             new_name = unique_name(path_2024, filename )
             final_path = os.path.join(path_2024, new_name)
             shutil.move(filename_path, final_path)
             logger.info(f"Moved {filename} moved to /2024")
         elif age_days > 90 and human_time.year == 2025:
             new_name = unique_name(path_2025, filename )
             final_path = os.path.join(path_2025, new_name)
             shutil.move(filename_path, final_path)
             logger.info(f"Moved {filename} moved to /2025")
        except Exception as e:
            print("Couldn't move file/s to destination")
            logger.error(f"Error moving {filename}: {e}")


