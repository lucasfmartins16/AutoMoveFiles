# import time module, Observer, FileSystemEventHandler
import time 
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler
import shutil
import datetime
import os


destiny = '/Users/Entrevos/Documents/ProjectX/screenshots/'

class OnMyWatch: 
    # Set the directory on watch 
  
    def __init__(self): 
        self.observer = Observer() 
  
    def run(self, a): 
        event_handler = Handler() 
        watchDirectory = a
        self.observer.schedule(event_handler, watchDirectory, recursive = True) 
        self.observer.start() 
        try: 
            while True: 
                time.sleep(5) 
        except: 
            self.observer.stop() 
            print("Observer Stopped") 
  
        self.observer.join() 
  
  
class Handler(FileSystemEventHandler): 
  
    @staticmethod
    def on_any_event(event): 
        if event.is_directory: 
            return None
  
        elif event.event_type == 'created': 
            # Event is created, you can process it now 
            print("Watchdog received created event - % s." % event.src_path) 
        elif event.event_type == 'modified': 
            # Event is modified, you can process it now 
            print("Watchdog received modified event - % s." % event.src_path)
            current = datetime.datetime.now()
            dir_name = '/Users/Entrevos/Documents/ProjectX/screenshots/' + str(current.year) + '-' + str(current.month) + '-' + str(current.day)
            if not os.path.isdir(dir_name):
                os.mkdir(dir_name)

            name = str(current.day) + '-' + str(current.month) + '-' + str(current.minute) + '-' +str(current.second)
            path = f'{dir_name}/{name}.png'
            shutil.move(event.src_path, path)

if __name__ == '__main__':
    a = input("Origin Directory Path:")
    destiny = input("Destination Directory Path:")
    watch = OnMyWatch() 
    watch.run(a)