# name = "aung min oo"
# print(name.upper())
class Car : 
    sterring = 1 #class level attribute
    def __init__(self,name,wheels) : #instant level attribute
        self.name = name
        self.wheels = wheels

    def drive(self) :
        print(f'{self.name} is driving')

    @classmethod
    def common(cls):
        print(f'all car have only {cls.sterring} sterring wheel')

lambo = Car("lamboghini",4)
marcedes = Car("marcedes",6)
lambo.common()
# print(Car.common())

# lambo.drive()
# print(lambo.name)
# print(lambo.wheels)

# marcedes.drive()
# print(marcedes.name)
# print(marcedes.wheels)

