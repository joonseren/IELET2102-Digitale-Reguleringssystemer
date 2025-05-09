## Oppgave 2c)

import threading
import time
import random

# Global variables
number = 0
mtx = threading.Lock()
mtxReader = threading.Lock()
readerCount = 0


def reader(id):
    global number, readerCount
    while True:
        time.sleep(random.uniform(0, 2))    

        # Går inn i felles
        mtxReader.acquire()
        if readerCount == 0:
            mtx.acquire()
        readerCount += 1
        print(readerCount)
        mtxReader.release()

        print(f"Reader thread {id} reading variable number as {number}")
        time.sleep(1)

        mtxReader.acquire()
        readerCount -= 1
        if readerCount == 0:
            mtx.release()
        mtxReader.release()


        


def writer(id):
    global number
    while True:
        time.sleep(random.uniform(0, 2))    
        
        mtx.acquire()
        number = random.randint(0, 10)
        print(f"Writer thread {id} setting variable value to {number}")
        mtx.release()


def main():
    readers = []
    writers = []
    for i in range(2):
        r = threading.Thread(target=reader, args=[i + 1])
        readers.append(r)
        r.start()
    
    for i in range(5):
        w = threading.Thread(target=writer, args=[i + 1])
        writers.append(w)
        w.start()
    
    for r in readers:
        r.join()
    for w in writers:
        w.join()
        
        
    


main()
