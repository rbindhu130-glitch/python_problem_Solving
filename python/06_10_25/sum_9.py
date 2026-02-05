'''Write a function to find the sum of numbers from 1 to n.
'''
def sum_to_n(n):
    # write your code here
    sum=0
    start = 1
    while start<=n:
        sum=sum+1
        start=start+1
    print(sum)    

sum_to_n(5)
sum_to_n(10)
sum_to_n(3)