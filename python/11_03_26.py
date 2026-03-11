
k = 3
lst = [1,2,3,4,5,6,7,8,9,10]

result = []
temp = []

for num in lst:
    temp.append(num)

    if len(temp) == k:
        result.append(temp)
        temp = []

if temp:
    result.append(temp)

print(result)
