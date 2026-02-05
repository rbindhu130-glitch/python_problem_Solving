time = int(input("enter your time (24 hours):"))
if 9<time and time<12:
    print("Morning Show")
elif 12<= time and time <16:
    print("Matinee show")
elif 16<= time and time<20:
    print("Evening Show")
else:
    print("night Show")            