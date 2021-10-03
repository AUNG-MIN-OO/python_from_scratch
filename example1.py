person = {}

while True : 
    name = input('name : ')
    age = input('age : ')

    # person['name'] = name;
    # person['age'] = age
    person [name] = age

    wantBreak = input('stop add? "y/n"')
    if wantBreak == "y" :
        print("stopped")
        break

ages = list(person.values())
print (ages)

i=0
for age in set(ages) :
    count = ages.count(age)
    print(f'{age} years old - {count}')
# print (person.items())

# for (key,value) in person.items() :
#     print (f"{key} is {value}")