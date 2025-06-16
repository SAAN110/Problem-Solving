num = 1
for i in range(1, 5): 
    for j in range(1, i + 1):  
        print(num, end=" ")
        num += 1
    print()
    
    
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(6, 0, -1):  
    for j in range(i):  
        print(alphabet[j], end=" ")  
    print()

for i in range(8):  
    print(f"{i:03b}")

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rows = 4  # Number of rows for the pattern

for i in range(1, rows + 1):
    for j in range(i):
        print(alphabet[j], end=" ")
    print()
    rows -= 1  # Decrease the number of rows after each iteration
