def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
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

print("The LCM is: ",lcm(num1,num2))

