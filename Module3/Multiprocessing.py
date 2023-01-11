import multiprocessing as mp
import math
import time

class MultiProcessing(mp.Process):
    def __init__(self, number):
        self.number = number

    def calculate_one(self):
        self.r = []
        for i in range(self.number):
            self.r.append(i ** 2)
        print(self.r)

    def calculate_two(self):
        self.r1 = []
        for i in range(self.number):
            self.r1.append(i ** 3)
        print(self.r1)
    def run(self):
        self.calculate_one()
        self.calculate_two()


if __name__ == '__main__':
    multi = MultiProcessing(10)

    s_time = time.perf_counter()
    multi.run()
    e_time = time.perf_counter()
    print(e_time - s_time)
