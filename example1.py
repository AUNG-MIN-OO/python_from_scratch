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

print (person)
print (person.items())

for (key,value) in person.items() :
    print (f"{key} is {value}")