def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


arr = [10,11,22,33,40,55,72,85] 
target = 55
result = binary_search(arr, target)

if result != -1:  # Fix: Check 'result' instead of 'target'
    print(f"{target} is found at index {result}")
else:    
    print(f"{target} is not found")

