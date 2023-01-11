import multiprocessing as mp
import math
import time
import os

class MultiProcessing(mp.Process):
    # def __init__(self, number):
    #     self.number = number
    #
    # def calculate_one(self):
    #     self.r = []
    #     for i in range(self.number):
    #         self.r.append(i ** 2)
    #     print(self.r)
    #
    # def calculate_two(self):
    #     self.r1 = []
    #     for i in range(self.number):
    #         self.r1.append(i ** 3)
    #     print(self.r1)
    def __init__(self):
        pass
    def search_folder(path, filename):
        flag1 = False
        for root, dir, files in os.walk(path):
            if filename in files:
                flag1 = True
                print("exits")
                print(os.path.join(root, filename))
        if flag1 == False:
            print("not exists")

    def search_drive(drive, name):
        flag = False
        for root, dir, files in os.walk(drive):
            for name1 in files:
                if name in name1:
                    flag = True
                    print("exists")
                    # Level1 task3 function
                    print(os.path.join(root, name))
                    break
        if (flag == False):
            print("not exist")
    def run(self):
        self.search_folder("c://Hcl_folder","hcl_program3.txt")
        self.search_drive("c://","hcl_program3.txt")


if __name__ == '__main__':
    multi = MultiProcessing()

    s_time = time.perf_counter()
    multi.search_drive("c:/","hcl_program3.txt")
    e_time = time.perf_counter()
    print(e_time - s_time)
