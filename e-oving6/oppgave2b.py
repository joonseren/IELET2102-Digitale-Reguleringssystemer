## Oppgave 2b)

import threading
import time

# global variables
limit = 20
number = 0
countFlag = True

def increment(id):
    global number, countFlag
    while countFlag:
        print(f"Thread {id} incrementing variable: {number}")
        number += 1
        time.sleep(0.5)

def reader(id):
    global number, limit, countFlag
    while countFlag:    
        if number >= limit:
            print(f"Thread {id} setting flag")
            countFlag = False
            break


def main():
    thread1 = threading.Thread(target=increment, args=[1])
    thread2 = threading.Thread(target=reader, args=[2])

    print("Starting threads")
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Main program detected flag change, exiting")


main()


