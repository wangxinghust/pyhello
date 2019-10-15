# 处理FileNotFound异常
filename='alice.txt'

try:
    with open(filename) as f_obj:
        contents=f_obj.read()
except FileNotFoundError:
    msg="sorry, the file "+ filename+" does not exist."
    print(msg)
else:
    # 计算文件大致包含多少个单词，效率较低
    words=contents.split()
    num_words=len(words)
    print("the file "+filename+" has about "+str(num_words)+"words.")