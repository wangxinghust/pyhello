from car import Car,ElectricCar
print("-----------分割继承")

my_beetle=Car('volkswagen','beetle',2016)
print(my_beetle.get_descriptive_name())
my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())

print("-------再次分割")
# 导入整个模块
import car
my_beetle=car.Car('vo','be',2011)
print(my_beetle.get_descriptive_name())

# 导入模块中所有的类，不推荐使用，不明确导入了哪些东西
from car import *