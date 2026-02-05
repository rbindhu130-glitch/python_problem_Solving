n= int(input("enter two digit number:"))
a = n//10
b = n%10

c = a+b
d = a*b

if c+d==n:
    print("great")
else:
    print("not")    