import time
import concurrent.futures
import threading
t1=time.perf_counter()
def something(sec):
    print(f"slepping {sec}")
    time.sleep(sec)
    print(f"done sleeping {sec}")
threads=[]
sec=[1,2,3,4,5]
for i in sec:
    t=threading.Thread(target=something,args=(i,))
    threads.append(t)
    t.start()
for thread in threads:
    thread.join()
t2=time.perf_counter()
print(t2-t1)