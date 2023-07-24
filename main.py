import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import FileCreatedEvent
from watchdog.observers.fsevents import FSEventsObserver
import sys

#nohup python3 main.py &

class DownloadsHandler(FileSystemEventHandler):

    def on_created(self, event):

        path = event.src_path
        extension = self.parse_extension(path)
        filename = os.path.basename(path)
        print(f"File extension: {extension}")
        if extension == '.pdf':
            dest_dir = "/Users/lucassimpson33/Downloads/PDF"
            dest_path = os.path.join(dest_dir, filename)
            os.rename(path, dest_path)
            print(f"Moved file to {dest_path}")
        elif extension == '.jpg':
            dest_dir = "/Users/lucassimpson33/Downloads/JPG"
            dest_path = os.path.join(dest_dir, filename)
            os.rename(path, dest_path)
            print(f"Moved file to {dest_path}")
        elif extension == '.exe':
            dest_dir = "/Users/lucassimpson33/Downloads/EXE"
            dest_path = os.path.join(dest_dir, filename)
            os.rename(path, dest_path)
            print(f"Moved file to {dest_path}")
        elif extension == '.html':
            dest_dir = "/Users/lucassimpson33/Downloads/HTML"
            dest_path = os.path.join(dest_dir, filename)
            os.rename(path, dest_path)
            print(f"Moved file to {dest_path}")
        elif extension == '.dmg':
            dest_dir = "/Users/lucassimpson33/Downloads/DMG"
            dest_path = os.path.join(dest_dir, event)
            os.rename(path, dest_path)
            print(f"Moved file to {dest_path}")
        elif extension == '.zip':
            dest_dir = "/Users/lucassimpson33/Downloads/ZIP"
            dest_path = os.path.join(dest_dir, event)
            os.rename(path, dest_path)
            print(f"Moved file to {dest_path}")
        elif extension == '.java':
            dest_dir = "/Users/lucassimpson33/Downloads/JAVA"
            dest_path = os.path.join(dest_dir, filename)
            os.rename(path, dest_path)
            print(f"Moved file to {dest_path}")

    def parse_extension(self, file):
        _, extension = os.path.splitext(file)
        return extension.lower()


    def on_modified(self, event):
        print(f"File or directory modified: {event.src_path}")

    def on_moved(self, event):
        print(f"File or directory moved from {event.src_path} to {event.dest_path}")


observer = FSEventsObserver()
observer.schedule(DownloadsHandler(), path='/Users/lucassimpson33/Downloads', recursive=False)
try:
    observer.start()
except Exception as e:
    print(f"An error occurred while starting the observer: {e}")
print(f"Observer is running: {observer.is_alive()}")


try:
    while True:
        time.sleep(1)
finally:
    observer.join()
    observer.join()















