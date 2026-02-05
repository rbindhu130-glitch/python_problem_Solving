'''
a=int(input("Enter a value :"))
b=int(input("Enter a value:"))
for i in range(b,a-1,-1):
    print(i)
    '''
'''a=int(input("Enter the number:"))
for i in range(2,a+1,2):
    print(i)'''
num = 15
shift_count = 0
for i in range(30):
    if num & 1:
        shift_count += 1
    num = num >> 1









