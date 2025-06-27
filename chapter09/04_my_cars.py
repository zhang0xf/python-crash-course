# 分别从每个模块中导入类
from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen','beetle',2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())

# 导入整个模块
import car
import electric_car

my_beetle = car.Car('volkswagen','beetle',2016)
print(my_beetle.get_descriptive_name())
my_tesla = electric_car.ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())