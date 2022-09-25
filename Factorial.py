def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))

x = int(input("Enter the number: "))

print("The factorial of", x, "with recursion is",factorial(5))

def factorialLoop(x):
    num = 1
    while x >=1:
        num = num * x
        x = x - 1
    return num

print("The factorial of", x, "with iteration is",factorialLoop(5))
