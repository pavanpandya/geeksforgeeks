num = int(input("Enter the Number: "))


def check_armstrong(num):
    # Converts 123 into [1, 2, 3]
    digits = [int(x) for x in str(num)]
    # print("Digits: ", digits)
    num_of_digits = len(digits)
    # print("Number of Digits: ", num_of_digits)

    sum = 0
    for i in digits:
        sum = sum + pow(i, num_of_digits)

    if sum == num:
        return 1


answer = check_armstrong(num)
if answer == 1:
    print(f"{num} is Armstrong Number")
else:
    print(f"{num} is not a Armstrong Number")
