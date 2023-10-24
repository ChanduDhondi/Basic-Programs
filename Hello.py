"""Hello World"""
print("This is my first Program")

i = [1,2,3,4,5,6]

def func(x):
    if x%2 == 0:
        return x**x

y = print(list(map(func,i)))

print([func(x) for x in i if x%2==0 ])
