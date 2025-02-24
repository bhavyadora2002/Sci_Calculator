import math
import sys

def square_root(x):
    if(x<0):
        return "Imaginary roots"
    return math.sqrt(x)


if __name__ == "__main__":
    
    if len(sys.argv) < 3:
        print("Invalid number of arguments")
    
    choice = int(sys.argv[1])
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])

    if choice == 1:
        print("Result:",square_root(num1))

    else:
        print("Please enter valid response")
