string = "1223455443"
enter = str(input("enter the string :"))
print(enter)
l1,l = list(string),[]
sum=""
for i in range(len(l1)):
    s=l1[i]
    for j in range(10):
        l1[i]=str(j)
        sum=''
        for k in l1:
            sum +=str(k)
        if int(sum)%3==0:
            l.append(sum)
    l1[i]=s
print(set(l))
print(f"count of values :",len(set(l)))