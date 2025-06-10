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
