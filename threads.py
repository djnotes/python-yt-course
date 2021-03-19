import threading
import zipfile
import time


class ZipThread(threading.Thread):
    def __init__(self):
        super().__init__()


    def run(self):
        print('Thread started.', threading.get_ident(), time.time())
        t = time.time()
        while time.time() - t < 2:
            print('Doing the job...')      
            time.sleep(1)      
        print('Thread finished.', threading.get_ident(), time.time())
        

zt = ZipThread()
ans = input('Start thread (y/N)?')
if ans == 'y':
    zt.start()

zt.join()
print(f'After thread call: {threading.get_ident()}', time.time())