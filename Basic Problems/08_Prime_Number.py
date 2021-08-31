start = int(input("Enter the Start Position: "))
end = int(input("Enter the Ending Position: "))


def check_prime(start_pos, end_pos):
    for i in range(start_pos, end_pos + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)


def check_prime_single_number(num):
    if num > 1:
        for i in range(2, int(num/2) + 1):
            if num % i == 0:
                print(f"{num} is not a Prime Number")
                break
        else:
            print(f"{num} is Prime Number")


check_prime(start, end)
check_prime_single_number(start)
