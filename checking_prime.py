#checking prime number or not
try:
    n = int(input("enter a number : "))
except:
    print("Number Can't be strint")
else:
    for i in range(2, n):
        if(n % i == 0):
            print(n, "is not a prime number")
            break
    else:
        print(f"{n} is not a Prime Number")
finally:
    print("Thank You!")