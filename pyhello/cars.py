cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.lower())

requested_topping='mushrooms'
if requested_topping!='anchovies':
    print("Hold the anchovies!")

answer=17
if answer!=42:
    print("That is not the correct answer. Please try again!")

requested_toppings=['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings) # 检查列表里是否包含相应的值
print('pepperoni' in requested_toppings)

age=19
if age>=18:
    print("you are old enough to vote")
else:
    print("sorry, you are too young to vate")
    print("please register to vote as soon as you turn 18")

age=12
if age<4:
    print("1")
elif age<18:
    print("2")
else:
    print("3")

requested_toppings.append('green peppers')
for requested_topping in requested_toppings:
    if requested_topping=='green peppers':
        print("sorry, we are out of green peppers right now.")
    else:
        print("Adding" + requested_topping.title() +".")
print("\nFinished making your pizza!")

# 检查列表是否为空
list1=[]
if list1:
    print("not null")
else:
    print("is null")

# 使用多个列表
available_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("adding "+requested_topping+'.')
    else:
        print("sorry, we don't have "+requested_topping+".")
print("finished making your pizza")