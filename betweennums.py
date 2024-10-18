a,b = map(int,input("Enter the Nubmers to display between a and b: ").split())
a,b = min(a,b)+1,max(a,b)

while a<b:
    print(a,end=" ")
    a+=1

