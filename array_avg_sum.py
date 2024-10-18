n = int(input("enter the number of Integers: "))
array =[]
i = 0 
while i <n:
    element = int(input("Enter the {0} Integer".format(i+1)))
    array.append(element)
    i+=1
print(array)
sum =0
for i in array:
    sum +=i
print(sum//n)

