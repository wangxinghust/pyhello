squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
    print(square)
print(squares)

digits=list(range(1,11))
print(min(digits))
print(max(digits))
print(sum(digits))

numbers=[value**2 for value in range(1,11)] # 列表解析
print(numbers)

# 4-3 数到 20 :使用一个 for 循环打印数字 1~20 (含)
for value in range(1,21):
    print(value)

# 4-9 立方解析 :使用列表解析生成一个列表,其中包含前 10 个整数的立方
numbers2=[value**3 for value in range(1,11)]
print(numbers2)