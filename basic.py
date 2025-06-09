a=234
print(a)
print('value of a is:',a)
num1=12
num2=12
print("the sum of num1 and num2 is: ", num1+num2)
num3="12"
num4="13"
print('the sum of num3 and num4 is: ', num3+num4)
x=123
print(type(x))
z=8
b=z
print("value of z is: ",z)
print('the value of b is: ',b)
Name=input('What is your name ?:')
print("Hello", Name , "!")
Age=int(input("Enter your current age: "))
AgeAfter2Years= Age+2
print("Your age now is:", AgeAfter2Years)

string_input = input("Enter a string: ")
frequency = {}
for char in string_input:
    frequency[char] = frequency.get(char, 0) + 1
for char, count in frequency.items():
    print(f"{char}: {count}")

sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print(f"Number of words: {word_count}")
