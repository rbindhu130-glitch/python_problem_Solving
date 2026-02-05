def signal(light):
    match light:
        case "RED":
            print("Stop")
        case "YELLOW":
            print("Get ready")
        case "GREEN":
            print("Go") 
        case _:
            print("Invalid Input") 
light=input("Enter the signal light:")
signal (light)                      
