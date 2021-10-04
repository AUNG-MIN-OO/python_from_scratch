# from car import Car

# lambo = Car("lamboghini",4)
# marcedes = Car("marcedes",6)
# lambo.common()

from Car.car import Car
from Car.functions import checkEngine

lambo = Car("lamboghini",4)
print(lambo.name)
checkEngine()