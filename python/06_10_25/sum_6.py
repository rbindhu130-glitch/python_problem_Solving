def count_odd(a, b):
    total = 0
    while a<=b:
        if a % 2!=0:
            total= total+1
        a = a+1
    print(total)   
    

count_odd(1, 10)
count_odd(5, 20)
count_odd(10, 15)
