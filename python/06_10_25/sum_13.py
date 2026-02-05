'''
Write a function to find how many un-popped balloons remain after n balloons are inflated.
 Every 4th balloon pops automatically.'''
def balloons_left(n):
    # write your code here
    count=0
    i =1
    while i<=n:
        if i %4!=0:
            count=count+1
        i = i+1
    print(count)        

balloons_left(4)
balloons_left(10)
balloons_left(20)