string = "123"
ln = len(string)
s_back = string
a1 = int(string)
#a = a1
s2 = ""
for i in range(ln,0,-1):
    #a = (a1//(10^(i+1))) * (10^(i))
    # a = a1//(10^(i*1))
    s1= str(a1 % (10^(i*1)))
    s2 = s2 + s1
    print(s2)
    for j in range(10):
        s =  str(a) + str(j)
        if (int(s)% 3 == 0):
            print(s)

