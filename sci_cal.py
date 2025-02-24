import math
import sys

def square_root(x):
    if(x<0):
        return "Imaginary roots"
    return math.sqrt(x)
def factorial(x):
    if(x<0):
        return "Enter positive number"
    return math.factorial(x)
def power(num1,num2):
    return num1 ** num2
def log(num1):
    if(num1<=0):
        return "Undefined"
    return math.log(num1)


if __name__ == "__main__":
    
    if len(sys.argv) < 3:
        print("Invalid number of arguments")
    
    choice = int(sys.argv[1])
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])

    if choice == 1:
        print("Result:",square_root(num1))
    elif choice == 2:
        print("Result:",factorial(num1))
    elif choice == 3:
        print("Result:", power(num1,num2))
    else:
        print("Please enter valid response")
