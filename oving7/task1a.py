## 1a)

import threading
import time
import random

threadAArrived = threading.Lock()
threadBArrived = threading.Lock()

threadAArrived.acquire()
threadBArrived.acquire()


def sleepFunctionA():
    sleepTime = random.randint(10, 500)/100
    print(f"Thread A going to sleep for {sleepTime} seconds")


    time.sleep(sleepTime)
    threadAArrived.release()
    print(f"Thread A waiting at rendezvous")
    threadBArrived.acquire()
    threadBArrived.release()
    print(f"Thread A finnsihed rendezvous")


def sleepFunctionB():
    sleepTime = random.randint(10, 500)/100
    print(f"Thread B going to sleep for {sleepTime} seconds")


    time.sleep(sleepTime)
    threadBArrived.release()
    print(f"Thread B waiting at rendezvous")
    threadAArrived.acquire()
    threadAArrived.release()
    print(f"Thread B finnsihed rendezvous")








def main():
    threadA = threading.Thread(target=sleepFunctionA)
    threadB = threading.Thread(target=sleepFunctionB)

    threadA.start()
    threadB.start()
    threadA.join()
    threadB.join()


    print("Both threads finished at rendezvous")



main()