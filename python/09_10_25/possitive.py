'''def odd_number(n):
    for i in range(n,0,-1):
        if i%2!=0:
            print(i)
odd_number(7)'''


def isPrime(num):

    if num <= 1:
        return False
    if num <= 3:
        return True     
    if num % 2 == 0 or num % 3 == 0:
        return False
  
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

print(isPrime(76))   # True
print(isPrime(10))  # False
