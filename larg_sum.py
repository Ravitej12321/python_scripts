n = []
i = int(input("enter the Number of integers"))
j = 0 
while j<i:
    k = int(input("enter the {0} integer : ".format(j+1)))
    n.append(k)
    j+=1
print(n)
large = 0
for x in n:
    if x >=large:large=x
print(large)

