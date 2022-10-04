a = int(input("What's the first number? "))
b = int(input("What's the second number? "))
r=a%b
while r:
    a=b
    b=r
    r=a%b
print('GCD is:', b)

