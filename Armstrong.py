n = int(input("enter the number to check:"))
a = str(n)
sum_1 = 0
for i in a:
    b = (int(i))**len(a)
    sum_1 = sum_1+b
if sum_1 == n:
    print(n," is an armstrong number.")
else:
    print(n," is not an armstrong number.")
