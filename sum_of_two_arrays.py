n = int(input("Enter the No.of Integers: "))
array1= []
array2,array3 =[],[]
i,j = 0,0 
while i <n:
    element = int(input("Enter the Integer  : "))
    array1.append(element)
    i+=1
print(array1)
while j < n:
    element= int(input("Enter the Integer: "))
    array2.append(element)
    j+=1
print(array2)
# array3 = array1+array2
for i in range(n):
    array3.append(array1[i]+array2[i])

print(array3)