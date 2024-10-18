list =[]
while True:
    n = int(input("Enter the Number: "))\
    
    if n >0:
        list.append(n)
    elif n==0 and len(list)>0:
        list.sort( reverse=True)
        print("largest Number {} and smallest Number {} in the list".format(list[0],list[-1]))
        break
    else :
        print("You Entered the Invalid Number")
        break
