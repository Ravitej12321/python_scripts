def binary_search(arr, target):
    size = len(arr)
    start = 0
    end = len(arr)-1
    arr.sort()
    print(arr)
    while (start<=end):
        middle = (start + end)//2
        if arr[middle] == target:
            return f"element found at location index {middle}"
        elif arr[middle] <= target:
            start = middle + 1
        elif arr[middle] >= target: 
            end = middle - 1
    return f"Not found"
list = [1,22,256,12,24]
target = 12
result = binary_search(list,target)
print(result)
