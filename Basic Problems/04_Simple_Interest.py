principle_amount = int(input("Enter your Principle Amount: "))
rate_of_interest = float(input("Enter the Rate of Interest: "))
time = float(input("Enter the Time Period in Years: "))


def simple_interest(principle_amount, rate_of_interest, time):
    simple_interest = (principle_amount * rate_of_interest * time) / 100
    print(
        f"Simple Interest on your amount - {principle_amount} at rate of interest - {rate_of_interest}% for time - {time} year is {simple_interest}")


simple_interest(principle_amount, rate_of_interest, time)
