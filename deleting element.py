import array

def deleteElement(arr,x):
    n=len(arr)
    # Find the index of the element to delete
    for i in range(n):
        if arr[i] ==x:
            index =i
            break

    if 0<= index <= n-1:
        # Shift elements left
        for i in range(index,n-1):
            arr[i] = arr[i+1]

        # Resize the array (actually remove last element)
        arr = arr[:n-1]

        return arr        # Create a new array with reduced size
    else:
        return arr        # Return the new resized array
    
arr = [11, 15, 6, 8, 9, 10]
x = 6   # Element to delete
outp = deleteElement(arr, x)
print("Modified array is:", outp)
