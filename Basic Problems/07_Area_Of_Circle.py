PI = 3.14

radius = float(input("Enter the Radius: "))

def AreaOfCircle(radius):
    return PI * (radius**2)

ans = AreaOfCircle(radius)
print(f"Area of Circle with radius {radius} is: {ans}")