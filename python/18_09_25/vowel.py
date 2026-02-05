def vowel(letter):
    letter=letter.lower()
    match letter:
        case 'a':
            print("vowel")
        case 'e':
            print("vowel")
        case 'i':
            print("vowel")
        case 'o':
            print("vowel")
        case 'u':
            print("vowel")
        case _:
            print("not")

letter=input("Enter your letter:")
vowel(letter)            