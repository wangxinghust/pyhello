# 写入文件
filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming! I love python!")

# 写入多行
with open(filename,'w') as file_object:
    file_object.write("I love programming!\n")
    file_object.write("I love python.\n")

# 附加文件
with open(filename,'a') as  file_object:
    file_object.write("继续添加\n")
    file_object.write("中文输入比英文还麻烦点\n")

# 读出先前写入的内容
with open(filename) as file_object:
    contents=file_object.read()
    print(contents)