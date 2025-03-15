## 2b)
from threading import Thread
import time

# Globle variabler
limit = 10
number = 0
flag = False

def writer(_id):
    global number, flag 
    while not flag:
        number += 1
        print(f"Thread {_id} incrementing variable: {number}")
        time.sleep(0.5)

def reader(_id):
    global flag, number
    while not flag:
        if number >= limit:
            print(f"Thread {_id} setting flag")
            flag = True
            break


def main():
    print(f"The incrementing limit is: {limit}")
    thread_1 = Thread(target=writer, args=[1])
    thread_2 = Thread(target=reader, args=[2])

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()
    print("Main program detected flag change, exiting")

main()    