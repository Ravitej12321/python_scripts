n = int(input("Enter the Number : "))

if n>0:
    i = 1
    while i<=n:
        if (n%i)==0:
            print(i,end=' ')
        i+=1
else: print("Enter the Valid Nubmer")