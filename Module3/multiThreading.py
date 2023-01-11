import os
#from searchfile import search_file1
from  threading import Thread
import time
def search_folder(path,filename):
    flag1=False
    for root,dir,files in os.walk(path):
        if filename in files:
            flag1=True
            print("exits")
            print(os.path.join(root,filename))
    if flag1==False:
        print("not exists")
def search_drive(drive,name):
    flag=False
    for root,dir,files in os.walk(drive):
        for name1 in files:
            if name in name1:
                flag=True
                print("exists")
                #Level1 task3 function
                print(os.path.join(root,name))
                break
    if(flag==False):
        print("not exist")
t1=Thread(target=search_folder,args=("c://Hcl_folder","hcl_program3.txt"))
t2=Thread(target=search_drive,args=("c://","hcl_program4.txt"))
#t2=Thread(target=search_file1,args=("c://","hcl_program2.txt"))
s_time=time.perf_counter()
t1.start()
t2.start()
t1.join()
t2.join()
e_time=time.perf_counter()
print(e_time-s_time)

