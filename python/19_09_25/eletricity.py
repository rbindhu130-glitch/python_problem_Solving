customer_type = input("Enter your type (Residential / Commercial:)")
unit = int(input("Enter unit:"))
bill=0
if customer_type== "Residential":
    if unit<=100:
        bill = unit*3
    elif unit >100 and unit <=200:
        bill = unit *5 
    elif unit >200:
        bill = unit*7    

elif customer_type=="Commercial":
    if unit <=100:
        bill = unit*5
    elif unit >100 and unit <=200:
        bill = unit*7
    elif unit >200:
        bill = unit*10
print("your bill is",bill)                