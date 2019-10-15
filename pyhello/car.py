class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回完整的描述性信息"""
        long_name = str(self.year)+' '+self.make+' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("this car has " + str(self.odometer_reading)+" miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        if miles < 0:
            return
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("用来在继承中测试子类覆盖父类的方法")


my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 通过实例直接修改属性的值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 通过方法修改属性的值
my_new_car.update_odometer(24)
my_new_car.read_odometer()

my_new_car.increment_odometer(50)
my_new_car.read_odometer()
print("---------------")
# 继承


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describle_battery(self):
        print("this car has a "+str(self.battery_size)+"-KWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "this car can go approximately " + \
            str(range)+" miles on a full charge"
        print(message)


class ElectricCar(Car):
    """电动汽车的独特"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("this car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_new_car.fill_gas_tank()
my_tesla.fill_gas_tank()

my_tesla.battery.describle_battery()
my_tesla.battery.get_range()