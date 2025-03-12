## 1b)

inputString = input("Insert the n-th Fibonacci number: ")
inputInt = int(inputString)

def fib(n):
    if n <= 0:
        print("Insert a valid number")
        return
    fibSeq = [0, 1]
    for _ in range(n - 2):
        fibSeq.append(fibSeq[-1] + fibSeq[-2])
    print(fibSeq[n - 1])

    
fib(inputInt)