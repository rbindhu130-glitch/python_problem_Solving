a = input("Select your path(Science/Commerce/Arts:)")

match a :
    case "Science":
       b = input ("Select your path(Medical/Engineering)")
       match b:
           case "Medical":
               print("Chosen path:Science → Medical")
           case "Enginerring":
               print("Chosen path:Science → Engineering")
           case _:
               print("not Science path")        
               

    case "Commerce":
        c = input("Select your path(CA/B Com)")
        match c:
            case "CA":
                print("Chosen path:Commerce→ CA")
            case "B Com":
                print("Chosen path:Commerce→ B Com")
            case _:
                print("not Commerce path")

    case "Arts":
        d = input("Select your path(History/Literature)")
        match d:
            case "History":
                print("Chosen path:Arts→ History")
            case "Literature":
                print("Chosen path:Arts→ Literature")
