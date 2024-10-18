n = int(input("Enter the Number : "))

print("*"*30)
print("\n")

li =[]
for i in range(1,n+1):
    k=1
    quo = 0
    while k <= i:
        if i%k==0:
            quo += 1
            k+=1
        else: k+=1
    if quo ==2: li.append(i)
print(li)
print("\n")
print("*"*30)