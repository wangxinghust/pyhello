bicycles=['trek','cannondale','readline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])
print("my first bicycle was a "+bicycles[0]+".")
bicycles[1]='cannon'
print(bicycles)
bicycles.append('catati')
print(bicycles)
bicycles.insert(0,'first')
print(bicycles)
del bicycles[0]
print(bicycles)
last_owned=bicycles.pop()
print(last_owned)
print(bicycles)
first_owned=bicycles.pop(0)
print(first_owned)
print(bicycles)
bicycles.remove('readline')
print(bicycles)
cars=['bmw','audi','toyota','subara']
cars.sort()
print(cars)
cars.sort(reverse=True) # 注意True的首字母是大写的T，小写的t会报错
print(cars)
print(sorted(cars)) # sorted 临时排e
cars.reverse() # 反e
print(cars)e
print("length is "+str(len(cars))) # len 求列表长度