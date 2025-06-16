for number in range(1, 11):
    square = number ** 2
    print(f"The square of {number} is {square}")
    
number = int(input("Enter a number: "))
print(f"Multiplication table for {number}:")
for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")   
    

    
n = 5 
for i in range(1, n+1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

n = 5 
for i in range(n):
    print(' ' * (i) + '*' * (n - i))

n = int(input("enter terms:"))
a = 0
b = 1
print(str(a)+","+str(b), end=',')
for i in range(3,n+1):
    c= a+b
    print(c,end=",")
    a=b
    b=c
