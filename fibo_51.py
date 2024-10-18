
n = int(input("ENter the number"))

i=0
while i<=n:
    if i==0:
        print(i,end=' ')
        initial_num=0
        
    elif i==1:
        print(i,end=' ')
        cur_num=1
        
    else:
        sum=initial_num+cur_num
        print(sum,end=' ')
        initial_num,cur_num=cur_num,sum
    i+=1



    

    
    
    
    
    
    
    


