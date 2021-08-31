num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))


def find_max(*args):
    max = args[0]
    for i in args:
        if (i > max):
            max = i
    return max


answer = find_max(num1, num2)
print("Max of two numbers:", answer)
