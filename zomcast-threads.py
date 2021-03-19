import threading
import time

def job():
    print('Started job',threading.get_ident(),  time.time())
    start_time = time.time()
    while(time.time() - start_time < 3):
        print('Performing job...')
        time.sleep(1)
    print('Finished job', threading.get_ident(), time.time())


#First thread making way
thread1 = threading.Thread(target = job) 

#Second thread making way
class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()
    
    def run(self):
            print('Started job',threading.get_ident(),  time.time())
            start_time = time.time()
            while(time.time() - start_time > 3):
                print('Performing job...')
                time.sleep(1)
            print('Finished job', threading.get_ident(), time.time()) 


thread2 = MyThread()

print('Before running thread', threading.get_ident(), time.time())
thread1.start()
thread1.join()
print('After starting thread', threading.get_ident(), time.time())





