# Some Different operations with the List

pizzas = ['neapolitan pizza','greek pizza','indian pizza','butter pizza']

for pizza in pizzas :
    print(f"I like the {pizza.title()}")

print("i really love pizza!")

# Using Rang Function

for i in range(1,21):
    print(i)

# printing the odd numbers using the third parameter of range

for j in range(1,21,2):
    print(j)

# List with the multiple of three numbers

multiple = list(range(3,31,3))

for k in multiple:
    print(k)

# Cubes of first three numbers

cubes = []

for cube in range(1,11):
    cubes.append(cube**3)

print(cubes)

# Cubes of first three numbers using list comprehension

cubes = [cube**3 for cube in range(1,11)]
print(cubes)

#Creating the list of multiple items

items = ['apple','banana','pomegranet','graphs','pineapple','guva','avacado','chiku','orange']

print("The first three items in the list are :",items[:3])

print("The three items from the middel of the list are :",items[3:6])

print("The last three items in the list are :",items[-3:])

