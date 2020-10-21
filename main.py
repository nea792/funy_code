from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import json
import os
import time


class handel(FileSystemEventHandler):
    def on_modified(self,even):
        for filename in os.listdir(myfld):
            src=myfld+"/"+filename
            new_destination=des+"/"+filename
            os.rename(src,new_destination)
            

myfld="main-directory"
des="destination-directory"
event_handler=handel()
Observer=Observer()
Observer.schedule(event_handler,myfld,recursive=True)


Observer.start()
try :
    while True:
        time.sleep(10)
except KeyboardInterrupt:
        Observer.stop()
Observer.join()
