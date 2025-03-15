from threading import Thread, Lock

count = 0
mtx = Lock()

def incrementingFunction(iterations):
    global count
    for i in range(0,iterations):
        mtx.acquire()
        count = count + 1
        mtx.release()

def decrementingFunction(iterations):
    global count
    for i in range(0,iterations):
        mtx.acquire()
        count = count - 1
        mtx.release()

def main():

    global count

    iterations = 10000000
    for index in range(0,10,1):
        count = 0
        incrementing = Thread(target = incrementingFunction, args = [iterations])
        decrementing = Thread(target = decrementingFunction, args = [iterations])
        
        incrementing.start()
        decrementing.start()
        
        incrementing.join()
        decrementing.join()
        
        print("The final count is: %d" % (count))


main()
