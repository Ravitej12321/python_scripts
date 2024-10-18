n = []
i = int(input('Enter the Number of Integers :'))
x=0
while x<i:
    j= int(input("enter the Integer Number : "))
    n.append(j)
    x+=1

print(n)
sum = 0 
for x in n:
    sum +=x
print(sum)

