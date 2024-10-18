import math
x = float(input("enter the x value"))

term =1
sum =1
for i in range(1,11):
    term *=(x/i)
    sum +=term
print(sum)
print(math.exp(x))

