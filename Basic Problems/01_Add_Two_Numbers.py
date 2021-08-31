num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))


def add_num(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum


answer = add_num(num1, num2)
print("The sum of two numbers is:", answer)
