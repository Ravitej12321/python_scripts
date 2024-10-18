n = int(input("Enter the Number : "))
cnt = int(input("Enter the Number of primes you want: "))
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
    if quo ==2 and len(li)<cnt : li.append(i)
print(li)
print("\n")
print("*"*30)