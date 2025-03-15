from threading import Thread

count = 0
flag = 1

def incrementingFunction(iterations):
    global count
    global flag
    for i in range(0,iterations):
        while flag < 1: pass # Spin-lock         
        flag = flag - 1
        count = count + 1
        flag = flag + 1

def decrementingFunction(iterations):
    global count
    global flag
    for i in range(0,iterations):
        while flag < 1: pass # Spin-lock
        flag = flag - 1
        count = count - 1
        flag = flag + 1

def main():

    global count

    iterations = 1000000

    for index in range(0,10,1):
        count = 0
        incrementing = Thread(target = incrementingFunction, args = [iterations])
        decrementing = Thread(target = decrementingFunction, args = [iterations])
        
        incrementing.start()
        decrementing.start()
        
        incrementing.join()
        decrementing.join()
        
        print("The final count is: %d" % (count))
        print("The flag is: %d" % (flag))

main()
