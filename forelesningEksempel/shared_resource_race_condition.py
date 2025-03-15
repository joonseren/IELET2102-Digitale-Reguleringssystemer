from threading import Thread

count = 0

def incrementingFunction(iterations):
    global count
    for i in range(0,iterations):
        count = count + 1

def decrementingFunction(iterations):
    global count
    for i in range(0,iterations):
        count = count - 1

def main():
    global count
    iterations = 1000000

    for index in range(0,10):
        count = 0
        incrementingThread = Thread(target = incrementingFunction, args = [iterations])
        decrementingThread = Thread(target = decrementingFunction, args = [iterations])
        
        incrementingThread.start()
        decrementingThread.start()
        
        incrementingThread.join()
        decrementingThread.join()
        
        print("The final count is: %d" % (count))

main()
