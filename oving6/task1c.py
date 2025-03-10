## 1c)
import numpy as np

inputString = input("Insert polynomial on this form (a b c): ")
inputArr = np.array(inputString.split(), dtype=float)

def roots(arr):
    if len(arr) != 3:
        print("Insert valid parameters")
        return None
    
    a, b, c = arr[0], arr[1], arr[2]
    
    if (b**2 - 4*a*c) < 0:
        print("Imaginary numbers are not supported :(")
        return None 
    
    x1 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - np.sqrt(b**2 - 4*a*c))/(2*a)

    rootsOutput = [x1, x2]
    
    print(f"The polynominal gived by {arr} has roots {rootsOutput}")


roots(inputArr)