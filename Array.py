import array

def updateElement(arr, z, pos):
    n = len(arr)
    # Ensure the position is within bounds
    if pos < 0 or pos >= n:
        return arr  # No change if position is invalid

    # Update the element at the given position
    arr[pos] = z

    return arr  # Return modified array

A = [11, 15, 6, 8, 9, 10]
z = 100 # Element to update

posi = 2  # Position 

out = updateElement(A, z, posi)
print("Modified array is:",out )
