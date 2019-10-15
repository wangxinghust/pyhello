def greet_user():
    """显示简单的问候语"""
    print("hello")
greet_user()
def greet_user(username):
    """显示简单的问候语"""
    print("Hello, "+username.title()+"!")
greet_user("mike")
# greet_user() 没有重载？

def describle_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("I have a "+animal_type.title()+".")
    print("My "+animal_type.title()+"'s name is "+pet_name.title()+".")
describle_pet('hamster','harry')
describle_pet('dog','willie')
# 关键字实参
describle_pet(animal_type='hamster',pet_name='harry')
describle_pet(pet_name='willie',animal_type='hamster')

# 函数默认值 与C++一致，默认值列表放后面，否则会出现歧义
def describle_pet2(pet_name,animal_type='dog'):
    """显示宠物的信息"""
    print("I have a "+animal_type.title())
    print("my "+animal_type+"'s name is "+pet_name)
describle_pet2(pet_name='willie')
describle_pet2('luck')
describle_pet2(pet_name='harry',animal_type='hamster')