# 元组：不可变的列表
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
    print(dimension)

# 不能修改元组元素值，但可以重新给存储元组的变量赋值
dimensions=(400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# 相比于列表，元组是更简单的数据结构，生命周期内值不变化