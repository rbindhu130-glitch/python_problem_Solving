a = int(input("number1:"))
b = int(input("number2:"))
n = int(input("Enter divisible times:"))
 
while a<=b:
    if a%n==0:
        print(a) 
    a=a+1