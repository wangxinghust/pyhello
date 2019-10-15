# 首先创建一个列表，其中包含一些要打印的设计
unprint_designs=['iphone case','robot pendant','do decaheron']
completed_models=[]

# 模拟打印每个设计，直到没有需要打印的设计为止
# 打印每个设计后，都将其移至列表completed_models中
while unprint_designs:
    current_design=unprint_designs.pop()
    # 模拟根据设计打印3D模型的过程
    print("Printing model: "+current_design)
    completed_models.append(current_design)
# 显示打印好的模型
for model in completed_models:
    print(model)

# 用函数来做
def print_models(unprint_designs,completed_models):
    """
    打印每个设计，直到没有需要打印的设计
    打印每个设计后，都将其移至completed_models中
    """
    while unprint_designs:
        current_design=unprint_designs.pop()
        print("printing model: "+current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有设计"""
    for model in completed_models:
        print(model)

print("-----")
unprint_designs=['iphone case','robot pendant','do decaheron']
completed_models=[]
print_models(unprint_designs,completed_models)
show_completed_models(completed_models)

# 禁止函数修改列表，可以传递列表的副本
print_models(unprint_designs[:],completed_models)
print("--------")

# 传递任意数量的实参
def make_pizza(*toppings): # 将实参封装到元组中
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

def make_pizza(*toppings):
    """概述要制作的pizza"""
    print("\nmaking a pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra chees')
print("---------")

# 结合使用位置实参和任意数量实参
def make_pizza(size,*toppings):
    """概述要制作的pizza"""
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings")
    for topping in toppings:
        print("- "+topping)
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
print("-------------")

# 使用任意数量的关键字实参
def build_profile(first,last,**user_info):
    """创建一个菜单，其中包含我们知道的有关用户的一切"""
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key, value in user_info.items():
        profile[key]=value
    return profile
user_info=build_profile('albert','einstein',location='princeton',field='physics')
print(user_info)