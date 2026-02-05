age= int(input("Enter your age:"))

if age<12:
    if age %2==0:
        print(50-5)
    else:
        print("50")
elif 12<=59:
    if age %2==0:
        print(120-5)
    else:
        print("120")
elif age>=60:
    if age%2==0:
        print(80-5)
    else:
        print("80")                            