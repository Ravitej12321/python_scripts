n = int(input("enter the Number: " ))
sum = 0
for i in range(1,n+1):
    if i%2==0:
        sum +=i
print("sum of Even Numbers : {}".format(sum))


#######3using the While Loop 
num=2
sum = 0
while num<=n:
    if num %2==0: sum +=num
    num+=1
    
print(sum)


########using Formula 

if n%2==0:print((n*(n+2))//4)
else: print(((n+1)*(n-1))//4)