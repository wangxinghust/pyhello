# 字典
alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

# 添加键值对
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

# 修改字典中的值
alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print("original x-position: "+str(alien_0['x_position']))

if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3

alien_0['x_position']+=x_increment
print("new x-position: "+str(alien_0['x_position']))

del alien_0['speed']
print(alien_0)

favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'java',
    'phil':'go'
    }
print(favorite_languages)
print("sarah's favorite language is "+
    favorite_languages['sarah'].title()+
    ".")

user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    }
for key, value in user_0.items():
    print("\nkey: "+key)
    print("value: "+value)
for name, language in favorite_languages.items():
    print("name: "+name+"\nlanguage: "+language+"\n")
for name in favorite_languages.keys(): # .keys()可省略
    print(name)
if 'erin' not in favorite_languages.keys(): # keys()实际上返回一个列表
    print("erin, please take our poll!")
for name in sorted(favorite_languages.keys()):
    print(name.title()+", thank you for taking the poll.")
print("the following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
# 集合set去重
for language in set(favorite_languages.values()):
    print(language)

alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

aliens=[]
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10
    elif alien['color']=='yellow':
        alien['color']='red'
        alien['speed']='fast'
        alien['points']=15
for alien in aliens[:5]:
    print(alien)
print("-----")
print("total number of aliens: "+str(len(aliens)))

# 存储所有点pizza的信息
pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
    }
# 概述所点的pizza
print("you ordered a "+pizza['crust']+"-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)

favorite_languages={
    'jen':['python','c'],
    'sarah':['ruby','go'],
    'edward':['java','lua'],
    'phil':['c#','swift'],
    }
for name,languages in favorite_languages.items():
    print("\n"+name.title()+"'s favorite languages are:")
    for language in languages:
        print("\t"+language.title())
users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
        },
    }
for username,userinfo in users.items():
    print("\nusername: "+username)
    fullname=userinfo['first']+" "+userinfo['last']
    location=userinfo['location']
    print("\tfullname: "+fullname.title())
    print("\tlocation: "+location.title())