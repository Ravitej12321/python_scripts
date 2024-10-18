n = int(input("Enter the Number: "))
sum,i = 0,0
while n>0:
    i+=1
    sum +=n
    n=int(input("Enter the Number: "))
if n==0 and i!=0:print("Average of the Entered Nubmers : ",sum//i)
else : print("Entered the invalid number")


