n = int(input("enter the No.of Integers : "))
array =[]
for i in range(n):
    element = int(input("enter the {} integer : ".format(i+1)))
    array.append(element)
print(array)
asc_check = 0 
flag= False
for x in array:
    if x>asc_check:
        asc_check=x
    else:
        flag = True
        break
if flag==False:
    print("yeah !! {} is an ascending order".format(array)) 
else :
    print("oops!! {} not an ascending order".format(array))