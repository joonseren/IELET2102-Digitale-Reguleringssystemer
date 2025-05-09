## Oppgave 2a)

import threading

def helloWord(id):
    print(f"Hello word from thread {id}")

def main():
    thread1 = threading.Thread(target=helloWord, args=[1])
    thread2 = threading.Thread(target=helloWord, args=[2])

    print("Starting threads")
    thread1.start()
    thread2.start()

    print("Finishing program")

main()
