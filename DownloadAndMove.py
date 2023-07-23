import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir =input("Enter the path of the download folder, Use / in VSC: ")
to_dir = input("Enter the destination folder path: ")

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(event)
        print(event.src_path)
        name,extension=os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                fileName=os.path.basename(event.src_path)
                print("Downloaded"+fileName)
                path1=from_dir+"/"+ fileName
                path2=to_dir+"/"+extension
                path3=path2+"/"+fileName
                
                if(os.path.exists):
                    print("Directory Exist")
                    print("Moving"+fileName)
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    print("Making Directory")
                    os.makedirs(path2)
                    print("Moving"+fileName)
                    shutil.move(path1,path3)
                    time.sleep(1)
                    
                


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop()

    