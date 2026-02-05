name=["karthick","Indhu","Yalini","Muthu","Raji"]
salary=[80000,80000,75000,70000,72000]
max=salary[0]

for i in range (len(salary)):
    if max<salary[i]:
        max=salary[i]
print(max)

# for names,salarys in zip (name,salary):
#     if max==salarys:
#         print(names)


for i in range (len(salary)):
    if salary[i]==max:
        print(name[i])