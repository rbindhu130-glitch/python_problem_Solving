X = int(input("Enter a number1:"))
Y = int(input("Enter a number2:"))
Z = int(input("Enter a number3:"))
if X==Y==Z:
    print("Equilateral ")
elif X!=Y and Y!=Z and Z!=X:
    print("Scalene")
elif X==Y or Y==Z or Z==X:
    print("Isosceles")  
else:
    print("Not a valid triangle")      
