from car import ElectricCar
print("分割继承来的---------")

my_tesla=ElectricCar('tesla','model s','2016')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describle_battery()
my_tesla.battery.get_range()