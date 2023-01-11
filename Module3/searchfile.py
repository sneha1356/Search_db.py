import os
import time
import logging
from locatedrives import SearchEngine
import threading
from searchLogging import Filelog
from Search_db import SearchDB
from Exception_Class import File
class SearchFile(threading.Thread):
    def __init__(self,drive,name):
        super().__init__()
        self.drive=drive
        self.name=name


    def search_file1(self):
        try:
            flag=False
            file_paths=[]
            for i in self.drive:
                self.drive1=i+":\\"
                for root,dir,files in os.walk(self.drive1):
                    for name1 in files:
                        if self.name in name1:
                            flag=True
                            #print("exists")
                            #Level1 task3 function
                            path=os.path.abspath(os.path.join(root,self.name))
                            file_paths.append(path)
                            break
            if flag==False:
                raise File("File Not found")

        except File as f:
            print(f)
            logging.info(f)
        return file_paths
    def run(self):
        self.search_file1()
if __name__=='__main__':
    db = SearchDB()
    name=input("enter filename:")
    log=Filelog()
    row = db.searchDB(name)
    if row==0:

        locate = SearchEngine()
        search = SearchFile(locate.locate_Activedrives(),name)
        result=search.search_file1()
        if len(result)!=0:
            db.insertDB(result[0])
            logging.info(result[0])
    else:
        print("exits")