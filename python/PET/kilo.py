'''
a = int(input("Enter weight:"))
if a <=5:
    print("shipped cost:$10"+50)
elif 5<=20 :
    print("shipped cost:$20"+50%)
else:
    print("shipped cost:$50"+50%)    '''














f = input("Enter food type (P/B/S): ").upper()

if f not in ["P", "B", "S"]:
    print("Invalid Input")
    exit()

qty = int(input("Enter quantity: "))

if qty < 0:
    print("Invalid Input")
    exit()

# Calculate cost
if f == "P":
    cost = 200 * qty
elif f == "B":
    cost = 100 * qty
else:  # f == "S"
    cost = 50 * qty

total = cost + (cost * 0.05)
print("Total Bill: ₹", total)

