def merge_the_tools():
    fruits = "AABCAAADABCARRSD"

    n= 4
    m = len(fruits)
    k1 =m//n
    f,g=[],[]
    count =0

    for i in range(0,len(fruits)+1):
        j=0
        lenn = len(fruits)
        while j<=lenn:
            if  fruits[i:j]!="":
                        f.insert(-count,fruits[0:k1])
                        fruits = fruits[k1:]
                        lenn-=3
            else:
                 j+=1
    for i in f:

        lenn=len(i)
        j=0
        while j <lenn:
            k=0
            while k <lenn :
                    if i[j]==i[k] and j!=k:
                        i=i[:k]+i[k+1:]
                        lenn-=1
                    else: k+=1
            j+=1
        g.insert(count,i)
        count +=1
    for i in range(1,len(g)+1):
        print(g[-i])
if __name__=="__main__":
     #string,k = map(str,input().split())
     #print(type(k))
     #print(type(string))
     merge_the_tools()
     