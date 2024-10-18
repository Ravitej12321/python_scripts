n  =int(input("enter the NO.of integers : "))

array =[]

for i in range(n):
    element = int(input("Enter the {} element".format(i+1)))
    array.append(element)
print(array)
#shortest form using the list slicing 
rev_array = array[::-1]
print(rev_array)
i = 0
while i<(n//2):
    array[i],array[-(i+1)]=array[-(i+1)],array[i]
    i+=1
print(array)

    