def linear_search(arr,target):
    for i in range (len(arr)):
        if arr[i] == target:
            return i
    return -1
    
arr = [1,2,6,8,2]
target = 3
result = linear_search(arr,target)

if result != -1:
    print(f"{target} is found at index {result}")
else:
    print(f"{target} is not found in the list")
