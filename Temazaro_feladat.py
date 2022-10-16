##Elso feladat: faktorialis

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))


x = int(input("Enter the number: "))

print("The factorial of", x, "with recursion is", factorial(5))


def factorialLoop(x):
    num = 1
    while x >= 1:
        num = num * x
        x = x - 1
    return num


print("The factorial of", x, "with iteration is", factorialLoop(5))


##Második feladat: Hanoi tornyai


##Harmadik feladat: Előző három összege
def fibRec(x):
    if x == 0:
        return 0
    if x == 1 or x == 0:
        return 1
    else:
        return fibRec(x - 1) + fibRec(x - 2) + fibRec(x - 3)

##Negyedik feladat: Két tag szorzata

def ket_tag_szorzata()
{

}


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


##Két inputos feladatok

##Első feladat: LNKO nyers

def calc_gcd(num1, num2):
    if (num2 == 0):
        return num1
    else:
        return calc_gcd(num2, num1 % num2)


num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

result = calc_gcd(num1, num2)
print("GCD is : {}".format(result))

##Második feladat: LNKO iterativ

a = int(input("What's the first number? "))
b = int(input("What's the second number? "))
r = a % b
while r:
    a = b
    b = r
    r = a % b
print('GCD is:', b)


##Negyedik feladat: LNKO rekurziv

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


num_one = int(input('Enter a value for x: '))
num_two = int(input('Enter a value for y: '))
if num_two == 0:
    print(num_one)
else:
    print(gcd(num_one, num_two))


##Ötödik feladat: LKKT

def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm


num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

print("The LCM is", compute_lcm(num1, num2))


def lcm(x, y):
    t = x % y
    if t == 0: return x
    return x * lcm(y, t) / t


print("The LCM is: ", lcm(num1, num2))
