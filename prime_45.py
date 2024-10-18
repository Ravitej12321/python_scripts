n = int(input("Enter the Number : "))

print("*"*30)
print("\n")
quo,i = 0,1

while i<=n:
    if n%i==0:
        quo +=1
        i+=1
    else :
        i+=1
if quo == 2 : print("{} is a prime Number".format(n))
else : print("{} is not a Prime Number".format(n))
print("\n")
print("*"*30)
