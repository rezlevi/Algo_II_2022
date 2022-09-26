## with recursion

def fibRec(x):
    if (x == 0):
        return 0
    if (x == 1 or x == 0):
        return 1
    else:
        return (fibRec(x - 1) + fibRec(x - 2))




## with iteration

def fibIte(x):
    a = 0
    b = 1

    print(a, b, end=" ")
    while (x - 2):
        c = a + b
        a, b = b, c
        print(c, end=" ")
        x = x - 1



x = int(input("Give me the length of the fibonacci numbers: "))

print(fibIte(x))

for i in range(0,x):
    print(fibRec(i),end=" ")



