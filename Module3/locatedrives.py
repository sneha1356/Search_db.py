import os,string
from Exception_Class import File
import win32api
import time
class SearchEngine:
    def __init__(self):
        pass
    def locate_Alldrives(self):
        d=win32api.GetLogicalDriveStrings()
        d1=d.split('\0')[:-1]
        print(d)
    def locate_Activedrives(self):
        try:
            a = [x  for x in string.ascii_uppercase if os.path.exists(x + ":")]
            if a==[]:
                raise File("No Active drives are present in the system")
            else:
                return a
        except File as f:
            print(f)

search=SearchEngine()
search.locate_Alldrives()
print(search.locate_Activedrives())

