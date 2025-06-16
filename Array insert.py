import array

def insertElement(arr,x,pos):
    n = len(arr)
    if pos < 0 or pos > n:
        return arr
    
    arr.append(0)
    for i in range(n,pos,-1):
        arr[i] = arr[i-1]

    arr[pos] = x 

    return arr

A = [11, 15, 6, 8, 9, 10]
y = 20  # Element to insert
posi = 2  # Position 
outp = insertElement(A, y, posi)
print("Modified array is:", outp)
