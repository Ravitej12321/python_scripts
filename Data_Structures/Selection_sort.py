def selection_sort(arr):
    """
        type : int
        return : array
        args : list or array
    """
    end =len(arr)
    for passes in range(end):
        min_index = passes
        for j in range(passes+1,end):
            if arr[j] < arr[passes]: min_index=j
        arr[passes],arr[min_index]= arr[min_index],arr[passes]
        
    return arr
list = [2,1,0,24,12]
list1 = []
list2 = [24,12,2,1,0]

result = selection_sort(list)
result1 = selection_sort(list1)
result2 = selection_sort(list2)

print(f"sorted list {result},{result1},{result2}")
