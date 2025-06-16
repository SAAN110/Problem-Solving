def insertion_Sort(arr):
    for i in range(1,len(arr)):
        current = arr[i]
        previous = i-1
        
        while previous >=0 and arr[previous] > current:
            arr[previous+1] = arr[previous]
            previous -= 1
        arr[previous+1]=current
    #     print(f"Iteration {i}: {arr}")
    # return arr

arr = [4,1,5,2,3]
print("Original Array",arr)
insertion_Sort(arr)
print("Sorted Array",arr)
