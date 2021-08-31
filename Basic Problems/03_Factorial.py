num = int(input("Enter the Number: "))


# def factorial(num):
#     fact = 1
#     if (num == 0 or num == 1):
#         fact = 1
#     elif num < 0:
#         return 0
#     else:
#         for i in range(1, num + 1):
#             fact = fact * i
#     return fact

def factorial(num):
    return 1 if num == 0 or num == 1 else num * factorial(num-1)


answer = factorial(num)
print(f'Factorial of {num} is {answer}')
