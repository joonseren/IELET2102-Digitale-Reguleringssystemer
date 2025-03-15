from threading import Thread, Lock

lock_1 = Lock()
lock_2 = Lock()

def worker_thread_1():
    lock_1.acquire()
    print("Thread 1 acquired Lock 1!\n",flush=True)
    lock_2.acquire()
    print("Thread 1 doing work!\n",flush=True)
    lock_2.release()
    lock_1.release()

def worker_thread_2():
    lock_2.acquire()
    print("Thread 2 acquired Lock 2!\n",flush=True)
    lock_1.acquire()
    print("Thread 2 doing work!\n",flush=True)
    lock_1.release()
    lock_2.release()

def main():
    thread_1 = Thread(target = worker_thread_1)
    thread_2 = Thread(target = worker_thread_2)
    
    thread_1.start()
    thread_2.start()
    
    thread_1.join()
    thread_2.join()
    
    print("All work done!")

main()
