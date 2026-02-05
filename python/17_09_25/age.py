age=int(input("Enter your age:"))
if age<5 and age>0:
    print("Free")
elif age>=5 and age<=12:
    print("10")
elif age>=13 and age<=64:
    print("20")
elif age>=65:
    print("15")
else:
    print("Invalid Input")              
