distance =float(input("Enter your traveled km:"))
fare = 0
if distance <=5:
    fare = distance*10
    print("your ola fare is :50")
elif distance >5  and distance <=15:
    fare = distance * 8
    print("your ola fare is:",fare)
else:
    fare = distance *6
    print("your ola fare is:",fare)