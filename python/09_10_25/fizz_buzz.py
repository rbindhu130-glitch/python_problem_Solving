def fizz_Buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n) 

def is_run_fizz_Buzz(n):
    for i in range(1,n+1): 
        fizz_Buzz(i)

is_run_fizz_Buzz(100)   