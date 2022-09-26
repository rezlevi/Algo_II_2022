## with recursion

def fib(x):
    if (x == 0):
        return 0
    if (x == 1 or x == 0):
        return 1
    else:
        return (fib(x - 1) + fib(x - 2))

x = int(input("Give me the length of the fibonacci numbers: "))

for i in range(0,x):
    print(fib(i),end=" ")

## with iteration
