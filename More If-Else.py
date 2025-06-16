user_age=int(input("enter your age:"))
if user_age<2:
    print("the person is a baby")
elif 2<=user_age<4:
    print("the person is a toddler")
elif 4<=user_age<13:
    print("the person is a kid")
elif 13<=user_age<20:
    print("the person is a teenager")
elif 20<=user_age<65:
    print("the person is an adult")
elif user_age>=65:
    print("the person is an elder")
    
year= int(input("Enter a year:"))
if ( year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("the entered number is a Leap Year")
else:
    print("the entered year is not a leap year")
