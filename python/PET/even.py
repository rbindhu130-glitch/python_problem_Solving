# a = int(input("Enter number1: "))
# b = int(input("Enter number2: "))
# count = 0

# if a <= b:
#     if a % 2 == 0:
#         count = count+a
#         a = a+1
# print(count)
# a = int(input("Enter number1: "))
# b = int(input("Enter number2: "))
# count = 0

# while a <= b:
#     if a % 2 == 0:  
#         count += a
#     else:            
#         a =a +1           
#     print(count)



# a = int(input("Enter a number1:"))
# b = int(input("Enter a number2:"))
# count = 0

# while a <= b:       
#     if a % 2 == 0:  
#         count =count+ a
#     a =a+ 1          
# print(count)


word="banana"
count=0
str=(input("Enter a char:"))
if str in word:
    for i in range(len(word)):
        if word[i]==str:
            print(i)   
else:
    print("not found")


# word = "I like python"

# for i in range (len(word)):




# str1 = "python"
# str2 = "notebook"
# list=[]
# for i in range(len(str1)):
#     if str1[i] in str2:
#         list.append(str1[i])
# print(list)
