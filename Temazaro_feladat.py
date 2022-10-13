##Elso feladat: faktorialis

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

##Második feladat: Hanoi tornyai


##Harmadik feladat: Előző három összege
def fibRec(x):
    if x == 0:
        return 0
    if x == 1 or x == 0:
        return 1
    else:
        return fibRec(x - 1) + fibRec(x - 2) + fibRec(x-3)

##Ötödik feladat: Előző kettő összege

## with recursion

def fibRec(x):
    if x == 0:
        return 0
    if x == 1 or x == 0:
        return 1
    else:
        return fibRec(x - 1) + fibRec(x - 2)


## with iteration

def fibIte(x):
    a = 0
    b = 1

    print(a, b, end=" ")
    while x - 2:
        c = a + b
        a, b = b, c
        print(c, end=" ")
        x = x - 1


x = int(input("Give me the length of the fibonacci numbers: "))

print(fibIte(x))

for i in range(0, x):
    print(fibRec(i), end=" ")

##Hatodik feladat: Tiz hatványai

def power(P):
    if P == 0:
        return 1

    return (10 * power(P - 1))


if __name__ == '__main__':
    P = 2

    print(power(P))

##Hetedik feladat: Kettő hatványai algoritmus

def power(P):
    if P == 0:
        return 1

    return (2 * power(P - 1))


if __name__ == '__main__':
    P = 2

    print(power(P))

