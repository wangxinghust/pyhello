# 异常
try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero!")

print("give me two number, I will divide them")
print("enter 'q' to quit")
while True:
    first_number=input("\nfirst number: ")
    if first_number=='q':
        break
    second_number=input("\nsecond number: ")
    if second_number=='q':
        break
    try:
        answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("you can't divide by zero!")
    else:
        print(answer)