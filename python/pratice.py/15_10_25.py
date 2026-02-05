#slicing
'''sentence = "I am Iron Man!"
sliced_str = sentence[5:9]
print(sliced_str)
#slicing without end
sliced_str = sentence[5:]
print(sliced_str)
sliced_str = sentence[:4]
print(sliced_str)

#slicing and concatenation

result_str = sentence[0] + sentence[4:]
print(result_str[::-1])


#Strides
result_str=sentence[::2]
print(result_str)

#Multi-line string
about_me = """Hi, I am Iron Man. 
I invented the arc reactor while being kidnapped.
I enjoy flying and blowing things.
Sometimes I save people in the process.
Billionaire, Playboy and a Philanthropist"""

print(about_me)

#Traversing through a string using loop.
# for i in range(len(sentence)):
#     print(sentence[i])

for ch in sentence:
    print(ch)



#tokenize 
words = sentence.split(" ")
for w in words:
    print(w)

joined_str = " ".join(words)
print(joined_str)
'''

'''
sentence = "apple"
total = 0

for i in range(len(sentence)):
    if sentence[i] in 'aeiouAEIOU':
        total = total + 1

print( total)
'''


'''sentence= "mango"

print(sentence[::-1])
'''
'''
list=["Raji","Yalini","Muthu"]
for name in list[::-1]:
    print(name)    '''

'''a=[1,14,-4,8,-7,-21,10]
total=0
for i in range (len(a)):
    if a[i]<0:
        total=total+1
print(total)    '''
'''
name = ["Indhu","Nanthini","Divya","Manju","Suthana","suya"]
marks = [60,80,70,99,88,50]

result =dict()

for i in range (len(name)):
    result[name[i]]=marks[i]
print(result)    

'''

student_dict={80:"Indhu",
             70: "Nanthini",
             95:"Divya",
             99:"Manju",
             82:"Suthana",
             67:"Suya"
}


for mark,name in student_dict.items():
    if mark>85:
        print(name)  
