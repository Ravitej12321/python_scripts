a,b = map(int, input("enter the two numbers : ").split())
a,b= max(a,b),min(a,b)

while a%b!=0:
    i = a%b
    b,a=i,b
print(b)