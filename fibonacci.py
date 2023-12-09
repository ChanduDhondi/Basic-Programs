
class Fibonacci:

    """fibonacci series"""
    def series(self,n):
        a = 0
        b = 1
        count = 1
        if n <= 0 :
            print("Pleaes enter the number greater than 0")
        else:
            print(f"Fibonacci Series upto {n} numbers is :")
            while count <= n:
                print(a)
                temp = a + b
                a = b
                b = temp
                count += 1        
    
    def number(self,n):
        a = 0
        b = 1
        i = 0
        if n <= 0:
            print('Please enter the number greater than 0')
        else:
            for i in range(1,n):
                c = a + b 
                a = b
                b = c         
            print(f"Fibonacci number at given position is :",b)

if __name__ == '__main__':
    n = int(input("Enter a Number : "))
    a = Fibonacci()
    a.series(n)
    a.number(n)
