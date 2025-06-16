def print2largest(arr):
    n = len(arr)

    if n < 2:
        print("Invalid Input!")
        return
    
    first = second = float(-1)

    for i in range(n):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] != first:
            second = arr[i]
    if second == -1:
        print("There is no 2nd largest element")
    else:
        print("The is 2nd largest element is:",second)

arr = [12, 35, 1, 10, 34, 1]
print2largest(arr)
