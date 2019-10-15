# 关键字with在不再需要访问文件后将其关闭，让pyhon自动之心close()
with open('pi_digits.txt') as file_object:
    contents=file_object.read()
    print(contents.rstrip()) # 删除读来的字符串末尾新增的空格，但测试中未新增空格

# 逐行读取
filename='pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip()) # 这里的rstrip用来消除读取到每行的换行符

# 创建一个包含文件各行内容的列表
with open(filename) as file_object:
    lines=file_object.readlines()
for line in lines:
    print(line.rstrip())

pi_string=''
for line in lines:
    pi_string+= line.strip()
print(pi_string)
print(len(pi_string))
digits=float(pi_string)
print(str(digits)) # 精度下降

# 读入大量数据
filename='pi_million_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
pi_string=''
for line in lines:
    pi_string+=line.strip()
print(pi_string[:52]+"...")
print(len(pi_string))

# 判断圆周率中是否包含自己的生日
birthday='010594'
if birthday in pi_string:
    print("your birthday appears in the first million digits of pi!")
else:
    print("your birthday does not appears in the first million digits of pi!")

# 字符串替换
message="I really like dogs."
print(message.replace('dog','cat'))