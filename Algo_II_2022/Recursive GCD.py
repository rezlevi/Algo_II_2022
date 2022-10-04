def gcd(x , y):
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

