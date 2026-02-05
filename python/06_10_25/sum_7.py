def count_divisible(a, b, n):
    # write your code here
    total=0
    while a<=b:
        if a%n==0:
            total=total+ 1
        a= a+1  
    print(total)      

count_divisible(1, 10, 2)
count_divisible(5, 25, 3)
count_divisible(10, 50, 5)


