def linear_search(arr,target):
    size = len(arr)
    start = 0 
    end = size - 1
    for  index in range(0,end):
        if arr[index] == target:return f"element found at location index {index}"
    return f"element not found"

list = [1,2,13,0,22]

target = 13

result = linear_search(list,target)

print(f"result1 is {result}")
target = 25

result2 = linear_search(list,target)

print(f"result2 is {result2}")