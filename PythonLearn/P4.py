# 注意for item in list：
# 冒号：
# 缩进
# 4-1
pizzas = ['pepperoni', 'margarita', 'hawaiian']
for pizza in pizzas:
    print("I like " + pizza + " pizza.\n")
print("I really love pizza!")

for value in range(1, 6):
    print(value)

# 4-3
for value in range(1, 21):
    print(value)
# 4-4
# for value in range(1, 1000001):
    # print(value)
# 4-5
numbers = list(range(1, 1000001))
print(numbers[0])
print(numbers[-1])
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4-6
odd_numbers = list(range(1, 21, 2))
for odd_number in odd_numbers:
    print(odd_number)

# 4-7
print("3的倍数")
divid_three = list(range(3, 31, 3))
for number in divid_three:
    print(number)

# 4-8
print("1-10的立方")
cubes = list(range(1, 11))
for cube in cubes:
    print(cube**3)

# 4-9
cubes = [cube**3 for cube in range(1, 11)]
print(cubes)


# list切片
players = ['0', '1', '2', '3', '4']
# [start:stop] 前闭后开
print("0-2")
print(players[0:3])
print("1-3")
print(players[1:4])
# [:stop] 从头开始，后开
print("0-3")
print(players[:4])
# 后开，倒数第三个不计入
print("0-2")
print(players[:-3])
# [start:] 从start开始，包括start，后闭
print("2-4")
print(players[2:])
print("2-4")
print(players[-3:])


# 4-10
slice_numbers = list(range(1, 11))
print("The first three items in the list are:")
print(slice_numbers[:3])

print("Three items from the middle of the list are:")
print(slice_numbers[3:6])

print("The last three items in the list are:")
print(slice_numbers[-3:])

# 4-11
pizzas = ['pepperoni', 'margarita', 'hawaiian']
friend_pizzas = pizzas[:]
pizzas.append('seafood')
friend_pizzas.append('cheese')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# 元组
# 元组的单个元素无法被修改，但是可以重新定义整个元组

# 4-13
fastfoods = ('hamburger', 'fries', 'cola', 'hotdog', 'pizza')
for fastfood in fastfoods:
    print(fastfood)
# fastfoods[0] = 'noodle'
fastfoods = ('noodle', 'fries', 'cola', 'hotdog', 'pizza')
for fastfood in fastfoods:
    print(fastfood)


