'''sentence = "Emma-is-a-data-scientist"
a = sentence.split('-')

for i in a:
    print(i)

'''


'''str1 = "Python"
reverse= str1[::-1]
print(reverse)'''

'''
string="Hello World"
string=string.lower()

vowels="aeiou"
count=0
for i in string:
    if i not in vowels and i!=" ":
        count=count+1
print(count)        
        '''
'''
string = "Python is awesome"
no_speace=""
for i in string:
    if i !=" ":
        no_speace=no_speace+i
print(no_speace)  
'''

'''special_char="!@#$%^&*"
password= input("enter a password:")
if len(password) >=8 and any(char in special_char for char in password):
    print("Password is strong")
else:
    print("Password is not strong")'''


'''try:

    a=int(input("enter a number:"))
    b=int(input("Enter a divition number:"))

    c=a/b
    print(f"Resent of dividing {a} + {b} = {c}")
except ZeroDivisionError:
    print("Your divition number is wrong")

except ValueError:
    print("You have enter valid number")    

except:
    print("some error")

'''




'''
while True:
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter a division number: "))

        c = a / b
        print(f"Result of dividing {a} by {b} = {c}")

    except ZeroDivisionError:
        print("You cannot divide by zero! Please enter again.")

    except ValueError:
        print("Invalid input! Please enter valid values.")

'''



numbers = [10, 5, 7, 8, 19, 19]
max_num = numbers[0]  
count = 0

for i in range(1, len(numbers)):
    if max_num < numbers[i]:
        max_num = numbers[i]
print(max_num)    
for i in range(len(numbers)):
    if max_num == numbers[i]:
        count += 1
print(count)