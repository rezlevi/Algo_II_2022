def calc_gcd(num1,num2):
    if(num2 == 0):
        return num1
    else:
        return calc_gcd(num2,num1%num2)

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

result = calc_gcd(num1,num2)
print("GCD is : {}".format(result))

