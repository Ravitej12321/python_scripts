def bubble_sort(arr):
    start = 0 
    end = len(arr)
    for  passes in range(end):
        
        for index in range(0,end-passes-1):
            
            if arr[index] >= arr[index + 1]:
                print(f"iteration no {passes+1}")
                arr[index],arr[index + 1] = arr[index + 1],arr[index]
    return f"sorted array using bubble sort is {arr}"

    

list = [5,4,3,1,2,21]

result = bubble_sort(list)

print(result)


