## 2c)

import threading
import time
import random

mutex = threading.Lock()
mutex_reader = threading.Lock()
countReaders = 0
variable = 0

def reader(_id):
    global variable, countReaders
    while True:
        time.sleep(random.uniform(0.5, 2.5))
        
        # Går inn i felles
        mutex_reader.acquire()
        if countReaders == 0:
            mutex.acquire()
        countReaders += 1
        mutex_reader.release()

        # Leser
        print(f"Reader thread {_id} reading variable value {variable}")
        time.sleep(1)

        # Går ut av felles
        mutex_reader.acquire()
        countReaders -= 1
        if countReaders == 0:
            mutex.release()
        mutex_reader.release()


def writer(_id):
    global variable
    while True:

        time.sleep(random.uniform(0.5, 2.5))
        
        number = random.randint(0, 100)

        mutex.acquire()
        variable = number
        print(f"Writer thread {_id} setting variable value to {number}")
        mutex.release()





def main():
    print("Starting")

    tw1 = threading.Thread(target=writer, args=[1])
    tw2 = threading.Thread(target=writer, args=[2])

    tr1 = threading.Thread(target=reader, args=[1])
    tr2 = threading.Thread(target=reader, args=[2])
    tr3 = threading.Thread(target=reader, args=[3])

    
    tw1.start()
    tw2.start()
    tr1.start()
    tr2.start()
    tr3.start()

    # tw1.join()
    # tw2.join()
    # tr1.join()
    # tr2.join()
    # tr3.join()

    # Holder main i livet
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Avsultter programmet")


main()