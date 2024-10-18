# a="   fly me   to   the moon  "
# b=a.strip()
# print(a.strip())
# print("hell0")
# print(len(a))
# print([i for i in b])
s="Heelo World"
b="Hello World"
s= s.strip()
s = s.split(" ")
print(s[-1])
a=[i for i in s]
print(a[-1])

import re 
strs = ["flower","flow","flight"]
x=re.findall("['f','l','o','w','e','r','s']",strs[1])
print(x)
y = re.findall(f"{x}",strs[2])
print(y)
x=''
for i in y:
    x=x+i
print(x)