import threading
import random
import time
 
# Dining philosophers, 5 Phillies with 5 forks. Must have two forks to eat.
 
class Philosopher(threading.Thread):
 
    running = True
 
    def __init__(self, xname, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.name = xname
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight
 
    def run(self):
        while(self.running):
            #  Philosopher is thinking (but really is sleeping).
            time.sleep(2)
            print ('%s is hungry.\n' % self.name, flush=True)
            self.dine()
 
    def dine(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight
 
        fork1.acquire(True)
        time.sleep(1) # Sleep inserted to ensure consistent deadlock
        fork2.acquire(True)
 
        self.dining()
        fork2.release()
        fork1.release()
 
    def dining(self):			
        print ('%s starts eating \n'% self.name, flush=True)
        time.sleep(2)
        print ('%s finishes eating and leaves to think.\n' % self.name, flush=True)
 
def DiningPhilosophers():
    forks = [threading.Lock() for n in range(5)]
    philosopherNames = ('Aristotle','Kant','Buddha','Marx', 'Russel')
 
    philosophers= [Philosopher(philosopherNames[i], forks[i%5], forks[(i+1)%5]) \
            for i in range(5)]
 
    Philosopher.running = True
    for p in philosophers: p.start()
    time.sleep(10)
    Philosopher.running = False
    print ("Now we're finishing.")
 
DiningPhilosophers()