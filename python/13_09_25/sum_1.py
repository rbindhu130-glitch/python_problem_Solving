# def sum_of_digits(num):
#     total = 0
#     a = num
#     while a >  0:
#         number = a % 10
#         total=total+number
#         a=a//10
#     return total
# num=int(input("Enter a number:"))

# print("sum of digits:",sum_of_digits(num))


#  def add_numbers(n):
#     numbers = []          
#     for i in range(1, n + 1):  
#         numbers.append(i)  
#     return numbers       


# print(add_numbers(9))  
# print(add_numbers(3))  



# def sum_odd_multiples7(num):
#     total=0
#     for i in range(1,num+1):
#         if i % 2 !=0 and i % 7==0:
#             total =total+i
#     return total

# print(sum_odd_multiples7(30))  
# print(sum_odd_multiples7(50))        

# FizzBuzz program (user decides the limit)

num = int(input("Enter a number: "))

# for i in range(1, num + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

num=int(input("Enter a number:")) 
for i in range (1,num+1):
    if i%2==0:
        print("not prime")
    else:
        print("prime")
