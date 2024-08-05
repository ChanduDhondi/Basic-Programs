""" Printing Prime Numbers """

n = int(input("enter your number"))

if n == 1 :
    print("Please Enter the Number Above 1")
else:
    for i in range(2,n+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)
                