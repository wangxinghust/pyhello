import pizza
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')

print("----------")
from pizza import make_pizza as mp 
mp(16,'pepperoni')
mp(12,'mushrooms','green peppers','extra cheese')

print("-----------2")
import pizza as p
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushrooms','green peppers','extra cheese')

# 导入模块中的所有函数
from pizza import *
make_pizza(16,'pp')
make_pizza(12,'gg','ff','dd')