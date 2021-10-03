# name = "aung min oo"
# print(name.upper())
class Car : 
    def __init__(self,name,wheels) :
        self.name = name
        self.wheels = wheels

    def drive(self) :
        print(f'{self.name} is driving')

lambo = Car("lamboghini",4)
marcedes = Car("marcedes",6)
lambo.drive()
print(lambo.name)
print(lambo.wheels)

marcedes.drive()
print(marcedes.name)
print(marcedes.wheels)
