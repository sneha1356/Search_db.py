import os
import locatedrives

def search_file1(drive,name):
    flag = False
    for i in drive:
        for root, dir, files in os.walk(i):
            for name1 in files:
                if name in name1:
                    flag = True
                    print("exists")
                    # Level1 task3 function
                    print(os.path.join(root, name))
                    break
    if (flag == False):
        print("not exist")
search_file1(locatedrives.locate_drives(),"hcl_program3.txt")