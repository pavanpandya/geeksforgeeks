# Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ....

nth_number = int(input("Enter the Number: "))
series = []


def fibonacci_sequence(n, series):
    if n < 0:
        return "Incorrect Input"
    elif n == 1:
        return series.append(0)
    elif n == 2:
        return series.append(1)
    else:
        a = 0
        b = 1
        series.append(a)
        series.append(b)
        for i in range(2, n):
            c = a + b
            series.append(c)

            a = b
            b = c

        return series


def nth_number_fibonacci_sequence(n):
    if n < 0:
        return "Incorrect Input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n):
            c = a + b
            a = b
            b = c

        return c


print(fibonacci_sequence(nth_number, series))
print(nth_number_fibonacci_sequence(nth_number))
