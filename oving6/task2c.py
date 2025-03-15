## 2c)
from threading import Thread, Lock
import time
import random

work = True
count_readers = 0
variable = 0

readLock = Lock()
mutLock = Lock()

def reading(_id):
    global count_readers, variable, work
    
    while(work):
        mutLock.acquire()
        if count_readers == 0:
            readLock.acquire()
        count_readers = count_readers + 1
        mutLock.release()
        
        print('>>> ', "Reader thread " + str(_id) + " reading variable value " + str(variable))
        time.sleep(1)
        
        mutLock.acquire()
        count_readers = count_readers - 1
        if count_readers == 0:
            readLock.release()
        mutLock.release()
        
        time.sleep(random.uniform(0,3))
        
    
def writing():
    global variable, work
    
    while(work):
        readLock.acquire()
        variable  =  random.randint(1, 10)
        print('>>> ', "Writer thread setting variable value " + str(variable))
        readLock.release()
        
        time.sleep(random.uniform(0,1))

def main():
    global work
    
    writer = Thread(target = writing)
    writer.start()
    
    N_readers = 3
    readers = [Thread(target = reading, args = (i+1,)) for i in range(N_readers)] 
    for reader in readers: reader.start()
    
    time.sleep(15)
    work = False


main()