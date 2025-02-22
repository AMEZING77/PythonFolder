# 3-1
names = ['WT', 'ZT', 'SW', 'XZH', 'QJH']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[-1])
print(names[-2])
print(names[-3])
print(names[-4])
print(names[-5])
# 3-2
message = "Hello, "
print(message + names[0] + "!")
print(message + names[1] + "!")
print(message + names[-1] + "!")
print(message + names[-2] + "!")

# 3-4
invited_persons = ['WT', 'ZT', 'SW', 'XZH', 'QJH']
print(invited_persons)

# 3-5
print(invited_persons[0] + " can't come.")
invited_persons[0] = 'ZJ'
print(invited_persons)

# 3-6
print("I found a bigger table.")
invited_persons.insert(0, 'AA')
invited_persons.insert(4, 'BB')
invited_persons.append('CC')
print(invited_persons)

# 3-7
print("I can only invite two persons.")
print("Sorry, " + invited_persons.pop() + ", I can't invite you.")
print("Sorry, " + invited_persons.pop() + ", I can't invite you.")
print("Sorry, " + invited_persons.pop() + ", I can't invite you.")
print("Sorry, " + invited_persons.pop() + ", I can't invite you.")
print("Sorry, " + invited_persons.pop() + ", I can't invite you.")
print("Sorry, " + invited_persons.pop() + ", I can't invite you.")
print("Hi, " + invited_persons[0] + ", you are still invited.")
print("Hi, " + invited_persons[1] + ", you are still invited.")
del invited_persons[0]
del invited_persons[0]
print(invited_persons)
print("The table is empty.")

#
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
sorted_cars = sorted(cars)
print(sorted_cars)
sortedReverse_cars = sorted(cars, reverse=True)
print(sortedReverse_cars)

# 3-8
places = ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Hangzhou']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))

places.reverse()
print(places)
places.reverse()
print(places)

places.sort()
print(places)
places.sort(reverse=True)
print(places)

# 3-9
print(len(invited_persons))
print(len(places))
