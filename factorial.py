#Factorial of given number
num = int(input("please enter the number"))
fact = 1
if (num == 0):
    print("The Factorial of given number is 1")
else:
    while num >= 1:
        fact = fact * num
        num -=1
    print("The Factorial of given number is ", fact)
