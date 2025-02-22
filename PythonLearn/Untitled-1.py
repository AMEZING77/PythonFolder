# 1,output name
name = "John Doe"
print(name)

# 2,intput name
name = input("What is your name? ")
print(name)

# 3,多行语句
list = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]
print(list)

# 4,多行注释
'''
This is a comment
written in
more than just one line
'''

# 5,缩进冒号：
if 5 > 2:
    if 4 > 3:
        print("Four is greater than three!")
    else:
        print("Four is not greater than three!")
else:
    print("Five is not greater than two!")

# 6,函数定义


def SayHello(date):
    print("Hello!", date)


SayHello("2025-02-11")
