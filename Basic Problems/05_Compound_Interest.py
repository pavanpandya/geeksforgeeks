# Information about Compound Interest:

# A = P(1 + R/100) t
# Compound Interest = A – P
# Where,
# A is amount
# P is principle amount
# R is the rate and
# T is the time span

principle_amount = int(input("Enter the Principle Amount: "))
rate_of_interest = float(input("Enter the Rate of Interest: "))
time = float(input("Enter the Time Period in Years: "))


def compound_interest(principle_amount, rate_of_interest, time):
    new_amount = principle_amount * (1 + (rate_of_interest/100))**time
    compound_interest = new_amount - principle_amount
    print(
        f"Compound Interest of {principle_amount} is {compound_interest}")


compound_interest(principle_amount, rate_of_interest, time)
