'''from arithmetic import my_add,my_mul,my_sub

num1=(float(input("Enter a number1:")))
num2=(float(input("Enter a number2:")))
operator=(input("+,-,*"))

def my_add (num1,num2):
        a=num1+num2
        print(a)'''




"""
Samples for type hints
"""
#Introducing type hints
import typing
def add(x:int, y:int) -> int:
    """
    name: add
    accepts two integers and returns their
    returns: integer
    """

    x = int(x)
    y = int(y)
    return (x + y)

def greeting(name):
    return f"Hello {name}"
print(add(10, 5))
greeting("Sachin")
greeting(90)


