def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))

number = int(input("Enter the number: "))

print("The factorial of", number, "is",factorial(number))