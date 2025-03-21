## 1b)

import threading
import random
import time

mutex = threading.Lock()
barrierLock = threading.Lock()

N_workers = 5
waitingCount = 0



def worker(_id):
    global waitingCount, N_workers

    # Soving
    sleepTime = random.randint(1, 5)
    print(f"<<Thread {_id}>>        Sleeping for {sleepTime}")

    time.sleep(sleepTime)

    # Ankomme barrier
    if waitingCount == 0: # hvis man er første må man låse porten
        barrierLock.acquire()

    mutex.acquire()
    print(f"<<Thread {_id}>>        Arrived at barrier")
    if waitingCount == 0: # hvis man er første må man låse porten
        barrierLock.acquire()
    waitingCount += 1
    mutex.release()

    #forlate
    if waitingCount == N_workers: # siste worker åpner porten
        print(f"<<Thread {_id}>>        Found all {N_workers} waiting, opening barrier")
        barrierLock.release()
        

def main():
    workers = []
    workerLocks = []

    for i in range(N_workers):
        workerLocks.append(threading.Lock())

    for lock in workerLocks:
        lock.acquire()    
   
    for i in range(N_workers):
       workers.append(threading.Thread(target=worker, args=[i+1]))
       workers[i].start()
    
    for thread in workers:
       thread.join()
    
    print(f"<<Main Thread>>     All threads through barrier")



main()
