import math
n,m = map(int,input("Enter the Number : ").split())

i = 2
k=1
while i <= n:
    ty= math.sqrt(i)

    if math.floor(ty)==ty and k<=m:
        print(i,end="\t")
        k +=1
    i+=1