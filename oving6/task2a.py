## 2a)

from threading import Thread


def helloWorld(_id):
    print(f"Hello world from thread {_id}")

def main():
    thread_1 = Thread(target=helloWorld, args=[1])
    thread_2 = Thread(target=helloWorld, args=[2])
    
    print("Starting threads")
    thread_1.start()
    thread_2.start()
    
    print("Finishing program")


main()