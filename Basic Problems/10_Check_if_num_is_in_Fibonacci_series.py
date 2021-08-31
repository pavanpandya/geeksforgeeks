# Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ....

# python program to check if x is a perfect square
import math

num = int(input("Enter the Number: "))


# A utility function that returns true if x is perfect square
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x


# Returns true if n is a Fibinacci Number, else false
def isFibonacci(n):

    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perferct square
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)


# A utility function to test above functions
if (isFibonacci(num) == True):
    print(f"{num} is a Fibonacci Number")
else:
    print(f"{num} is not a Fibonacci Number")
