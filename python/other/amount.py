amount = float(input("Enter your amount: "))
member = input("Are you a member? (yes/no): ")

if member == "yes":
   points = int(amount // 10)  
else:
   points = 0

print("Reward points earned:", points)







