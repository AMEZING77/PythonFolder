import this

print(this.__annotations__)
message = "Hello, World!"
print(message)
message = "Hello, Python!"
print(message)

name = "John Doe"
print(message + name.title())
print(name.upper())
print(name.lower())

quote = ('Albert Einstein once said,'
         '\"A person who never made a mistake never tried anything new."')
print(quote)
famous_person = "Albert Einstein"
message = (famous_person + ' once said,'
           '\"A person who never made a mistake never tried anything new."')
print(message)

name = "\n\tJohn Doe\t"
print(name + "hh")
print(name.lstrip() + "hh")  # 去掉左边的空格
print(name.rstrip() + "hh")  # 去掉右边的空格
print(name.strip() + "hh")  # 去掉两边的空格

print(3 * 2)
# 两个乘号（**）表示乘方运算：
print(3**2)
# 将任意两个数相除时，结果总是浮点数，即便这两个数都是整数且能整除：
print(4 / 2)
# 只要有操作数是浮点数，Python默认得到的总是浮点数
print(4.0 + 2)
# 多变量单行赋值
a, b, c = 1, 2, 3
print(a, b, c)

# 2-8
print(5 + 3)
print(10 - 2)
print(2 * 4)
print(16 / 2)

# 2-9
favorite_number = 8
message = "My favorite number is " + str(favorite_number) + "."
print(message)


