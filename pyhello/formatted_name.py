def get_formatted_name(first_name,last_name):
    """返回完整的姓名"""
    full_name=first_name+" "+last_name
    return full_name.title()
musician=get_formatted_name('jimi','hendrix')
print(musician)

def get_formatted_name(first_name,last_name,middle_name=''):
    """返回完整的姓名"""
    if middle_name:
        full_name=first_name+" "+middle_name+" "+last_name
    else:
        full_name=first_name+" "+last_name
    return full_name.title()
musician=get_formatted_name('jimi','hendrix')
print(musician)
musician=get_formatted_name('john','hooker','lee')
print(musician)

# 返回字典
def build_person(first_name,last_name):
    """返回一个字典，其中包含一个人的信息"""
    person={'first':first_name,'last':last_name}
    return person
musician=build_person('jimi','hendirx')
print(musician)

def build_person(first_name,last_name,age=''):
    """返回一个字典，其中包含一个人的信息"""
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
musician=build_person('jimi','hendrix',age=27)
print(musician)

# 无限循环
while True:
    print("\nplease tell me your name: ")
    print("enter 'q' at any time to quit")
    f_name=input("first name: ")
    if f_name=='q':
        break
    l_name=input("last name: ")
    if l_name=='q':
        break

    full_name=get_formatted_name(f_name,l_name)
    print("\nHello, "+full_name.title()+"!")

# 传递列表
def greet_users(nname):
    """向列表里的每位用户都发出简单的问候"""
    for name in nname:
        msg="hello, "+name+"!"
        print(msg)
usernames=['hannah','ty','margot']
greet_users(usernames)