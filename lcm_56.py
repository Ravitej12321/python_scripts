a,b =map( int,input("Enter two Numbers : ").split())
maximum = max(a,b)
while True:
    if maximum%b==0 and maximum%a==0:
        print(maximum)
        break
    maximum +=1
print(maximum)
# divisiors_a = []
# divisiors_b = []

# count = 0
# for i in range(1,a):
#     if a%i==0:
#        divisiors_a.append(i)

# print(divisiors_a)
# for i in range(1,b):
#     if a%i==0:
#        divisiors_b.append(i)    
# print(divisiors_b)
# # prod = max(divisiors_b,divisiors_a)
# # prodmin= min(divisiors_a,divisiors_b)
# # for i in prodmin:
# #     if b%i==0:
# #         lcm = (a*b)//i

# # print(lcm)


