list1 = [0,1,1,2,2,2,3,3,3,3]


def remove_element(nums):
    # array1 = array
    # count =0
    # for i in array:          # 1. first method.
    #     if i == val:
    #         count +=1
    # return len(array)-count
#     count = array.count(val)
#     for i in range(count):
#         array.remove(val)
#     return array
    
 
# result = remove_element(list1,value)
# print(result)
    nums2 = nums
    for i in nums:
        count = nums.count(i)
        while count>2:
            nums2.remove(i)
            count -=1
    print(nums2)
    return len(nums2)

result = remove_element(list1)
print(result)


#  nums2 = nums
#     for i in nums:
#         count = nums.count(i)
#         for j in range(count-1):
#             nums2.remove(i)
#     print(nums2)
#     return len(nums2)

# result = remove_element(list1)
# print(result)