# class vehicle:
#     def __init__ (self,
#          wheel,
#          speed,
#          fuel_type,
#          price):
        
#         self.wheel=wheel
#         self.speed=speed
#         self.fuel_type=fuel_type
#         self.price=price

#     def show_details(self):
#         print(f"self.wheel:{self.wheel}")  
#         print(f"self.speed:{self.speed}")
#         print(f"self.fuel_type:{self.fuel_type}")  
#         print(f"self.price:{self.price}")
#     def accumulate(speed):
#         self.speed+=10



# class car(vehicle):
#     def __init__(self):
#         super().__init__(wheel=4,speed=100,fuel_type="petrol",price=100000)


# my_car=car()
# my_car.show_details()     
# 
#  



# ele=[1,2,3,4,5]
# count=0
# total=0

# for i in range (len(ele)):
#     count=count+ele[i]
#     total=total+1
# avg=count//total
# remin= total-avg    

# print(remin)

# ele = [1,2,3,4,5]
# count = 0
# total = 0

# for i in range(len(ele)):
#     count = count + ele[i]
#     total = total + 1

# avg = count // total
# remin = total - avg

# print( avg)
# print( remin)



# word="pineapple"
# starting=word[0]
# for i in range (1,len(word)):
#     if word[i]<starting:
#         starting=word[i]
# print(starting)     

# def print_no_vowel(words):
#     #Enter you code here
# for i in range (0,len(words)):
#     if words[0]=="a"or"e"or"i"or"o"or"u":
#         print(words)
#         break   


# list="The quick brown fox jumps over the lazy dog"
# letter="abcdefghijklmnopqrstuvwxyz"
# for i in range(len(list)):
#     first=list.lower()
#     if first[i]==alp:
#         print("True")
#     else:
#         print("False")    


# inventory = {"apple":10,"banana":5,"mango":8}
# def fruit (productname,quantity):
#     if  productname in inventory :
#         inventory[productname] +=  quantity
        
#     else:
#         inventory[productname] = quantity
#     print(inventory)


# fruit ("apple",4)
# fruit ("orange",9)




# def numbers_between_two_zeros(arr):
#     start = -1
#     result = []

#     for i, val in enumerate(arr):
#         if val == 0:
#             if start == -1:
#                 start = i      
#             else:
#                 return result
#         elif start != -1:
#             result.append(val)

#     return -1



# print(numbers_between_two_zeros([5, 6, 0, 0, 9]))   
# print(numbers_between_two_zeros([5, 0, 3, 4, 0, 7]))
# print(numbers_between_two_zeros([1, 2, 3, 0, 7, 8])) 



# def highest_avg(first_list, second_list) :
#     #Enter your code here
#     count1=0
#     total1=0
#     count2=0
#     total2=0
#     for i in range(len(first_list)):
#             count1 +=1
#             total1 += first_list[i]
#     avg1 = total1 // count1
#     for i in range (len(second_list)):
#             count2 +=1
#             total2 +=second_list[i]
#     avg2 = total2 // count2
#     if avg1 > avg2:
#         print(first_list)
#     elif avg2 == avg1:
#         print("Both are equal")
#     else:
#         print(second_list)

	
# highest_avg([4, 1, 2, 3, 5], [1, 0, 0, 1, 2, 1, 0, 2])    
# highest_avg([5, 5, 5, 5],[2, 3, 4, 6, 10] )     
# highest_avg([6,4,7],[8,9,5])   
        
# str1 = "Anna went to America and met Adam"
# count = 0
# word = ""

# for i in range(len(str1)):
#     if str1[i] != " ":
#         word += str1[i]  
#     else:
#         if word[0].upper() == word[-1].upper(): 
#             count += 1   
#         word = "" 

# print("Count:", count)
    


# text = "apple banana temple apple cow anu"
# words = []
# word = ""

# for char in text:
#     if char != " ":
#         word += char
#     else:
#         if word not in words:
#             words.append(word)
#         word = ""

# if word != "" and word not in words:
#     words.append(word)

# print(len(words))       



# str="Johannesburg is the most populous city of South Africa"

# word=""
# long_word=""

# for i in range(len(str)):
#     if str[i] !=" ":
#         word+=str[i]
#     else:
#         if len(word)>len(long_word):
#             long_word=word
#         word=""
        
        
# if len(word) > len(long_word):
#     long_word=word
# print(long_word)   


# s = "Python is super powerful"

# smallest_word = "" 
# word = ""

# for char in s:
#     if char != " ":
#         word += char  
#     else:
#         if smallest_word == "" or len(word) < len(smallest_word):
#             smallest_word = word
#         word = ""  


# if smallest_word == "" or len(word) < len(smallest_word):
#     smallest_word = word

# print(smallest_word)



# str="hello"
# res=""
# for i in range(len(str)):
#     if i %2!=0:
#         res +="*"
#     else:
#         res +=str[i]
# print(res)    



# list = [2, 3, 4, 5]
# new=[]

# for i in range(len(list)):
#      list1=list[i] **2
#      new.append(list1)
# print(new)     
     
     
# list = [20, 60, 75, 45, 90, 35]
# k=50
# res=[]
# for i in range (len(list)):
#      if list[i] >k:
#          res.append(list[i])
# print(res)         
        
# list=[5, -3, 9, -8, 2]
# k=0
# res = []
# for i in range (len(list)):
#     if list[i] <k:
#         res.append (0)
#     else:
#         res.append (list[i])
        
        
# print(res)   
# numbers = [3, 5, 3, 8, 3, 9]
# target = 3
# count=0
# for i in range(len(numbers)):
#     if numbers[i]==target:
#         count+=1
# print(count)        

# str="Amma and appa is my anna"
# str1=str.lower()
# count=0
# a=str1.split()
# for i in range (len(a)):
#     if (a[i][0]) == (a[i][-1]):
#         count +=1
# print(count)



# * Electricity Usage Check
# Given a list of daily electricity usage (in units) for a week, print "Power Saving" if all values are below 100,
# otherwise print "High Usage Detected".(Hint: create a new variable called count,check if every element in the element is more than 100,
# if more than 100, increment the count ,do this till end of the list finally check if count is greater than zero
# if yes, print "High Usage Detected",else, print "Power Saving")



# daily_usage = [95, 88, 105, 76, 99, 85, 92]

# count = 0

# for usage in daily_usage:
#     if usage >= 100:
#         count += 1 
# if count > 0:
#     print("High Usage Detected")
# else:
#     print("Power Saving")



# list = [1,2,3,4,5,6]
# count =0
# for i in range(len(list)):
#     count +=1
# print(count)    
    

# list=[1,2,3,4,6,7,2,3]
# count=0
# k=2
# for i in range(len(list)):
#     if list[i]==k:
#         count+=1
# print(count)        

        
# s = "abcdefg"

# even = ""
# for i in range(len(s)):
#     if i % 2 == 0:
#         even = s[i] + even   

# result = ""
# ei = 0
# for i in range(len(s)):
#     if i % 2 == 0:
#         result += even[ei]
#         ei += 1
#     else:
#         result += s[i]

# print(result)




# list=[1,2,3,4,5,6]

# for i in range(len(list)):
#     if i %2 !=0:
#         list[i]=0
# print(list)        



# def compare_strings(word1,word2):

#     if len(word1) != len(word2):
#         print("Invaild")
#         return
#     count=0
#     for i in range(len(word1)):
#         if word1[i] !=word2[i]:
#             count+=1
#     if count==1:
#         print("Yes")
#     else:
#         print("no")
        
# compare_strings("apple","abble")    


# str="python"

# sum=""
# for i in range(1,len(str)):
#     if i %2!=0:
#         sum +=(str[i])
# print(sum[::-1])

# def book_shelf(books, newBook):
#     if books==0:  
#         return -1
    
#     for i in range(1, len(books)):
#         if books[i-1] >= newBook >= books[i]:
#             return i 
            
#     return len(books)

# Books = [98, 75, 60, 50, 40, 25]
# NewBook = 71

# print(book_shelf(Books, NewBook))  


# def book_shelf(books, newBook):
#     #Write your code here
#     n=-1
#     for i in range(len(books)):
#         if books[i] > newBook:
#             n =i+2
#     print(n)  
# book_shelf([98, 75, 60, 50, 40, 25], 55)



# str1 = "yalini,80|indhu,90|raji,60|gopi,70|anu,90"
# word = str1.split("|")

# max_mark = 0
# max_name = ""

# for ch in word:
#     name, mark = ch.split(",")
#     mark = int(mark)
#     if mark >= max_mark:
#         max_mark = mark
#         max_name = name

# print(max_name, max_mark)




# count=0
# for i in range(len(str)):
#     if str[i]=='n':
#         count+=1
# print(count)        



# def num(list):
#     sum=0
#     count=0
#     total=0
#     for i in range(len(list)):
#         count+=1
#         total+=list[i]

#     avg=total/count
#     for i in range(len(list)):
#         if avg< (list[i]):
#             sum+=1
#     print(sum)        

# num([10,20,30,40,50])



# def word(string):
#     word=""
#     for i in range(len(string)):
#         if string[i] not in word or word=="":
#             word+=(string[i])

#     print(word)            
# word("programming")

# def word(sentence):
#     words = sentence.split()
#     longest_word = ""
#     for word in words:
#         if len(word) > len(longest_word):
#             longest_word = word

#     print(longest_word)
# word("Python makes programming enjoyable")

    

# str="This is yellow aeiou colours"
# count1=0
# count2=0

# word= str.split(" ")
# for ch in word:
#     for i in range(len(ch)):
#         if ch[i] in "aeiouAEIOU":
#             count1 +=1
#             if count1 > count2:
#                 count2 =count1
# print(ch)                


s = "This is yellow aeiou colours"
max_vowels = 0
max_word = ""

words = s.split()

for word in words:
    count = 0
    for ch in word:
        if ch in "aeiouAEIOU":
            count += 1

    if count > max_vowels:
        max_vowels = count
        max_word = word

print(max_word)



