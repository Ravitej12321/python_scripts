# list = []
# # for iterator in range(start index, end index):
# for  i in range(1,11):
#     list.append(i)
# print(list)
prices = [7,1,3,5,6,4]
min = 0
index = 0
for i in range(len(prices)-1):
    if prices[i]<prices[i+1]:
        min = prices[i]
        index = i
max = max(prices[index:])
print(max-min)

