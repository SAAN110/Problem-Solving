test= [1, 2, 3, 4,5]
print(*test)

def print_function(A):
    for a in A:
        print(a + '1')
print_function(['a', 'b', 'c'])


def safe_divide(numerator, denominator):
    try:
        result = numerator/denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot Divide By Zero")
        return None
numerator=int(input("Enter the numerator value:-"))
denominator=int(input("Enter the denominator value:-"))
print(safe_divide(numerator,denominator))
from collections import namedtuple

# Input number of students
n = int(input("Enter number of students:"))

# Input the names of the fields
fields = input("Enter the number of fields:").split()

# Create the named tuple class with the given fields
Student = namedtuple('Student', fields)

# Initialize a list to store the student records
students = []

# Read the student data
for _ in range(n):
    students.append(Student(*input().split()))

# Compute the average marks
total_marks = sum(int(student.MARKS) for student in students)
average_marks = total_marks / n

# Print the average marks
print(f"{average_marks:.2f}")
