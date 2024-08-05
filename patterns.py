class Patterns:

    @classmethod
    def rectangle(cls, width, height):
        for _ in range(0,height):
            for i in range(0,width):
                print('*', end=' ')
            print()
    
    @classmethod
    def hollowSquare(cls, width, height):
        # End points logic
        for i in range(0, height):
            for j in range(0, width):
                if (i==0 or i==height-1 or j==0 or j==width-1):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()

        for i in range(0, height):
            if i == 0 or i == height-1:
                print('*'*width)
            else:
                print('*'+' '*(width-2)+'*')

    @classmethod
    def numberIncreasingPyramid(cls, rows):
        for i in range(0,rows):
            for j in range(0,i+1):
                print(j,end=' ')
            print()

    @classmethod
    def numberIncreasingReversePyramid(cls, rows):
        for i in range(rows,0,-1):
            for j in range(0,i):
                print(j, end=' ')
            print()

    @classmethod
    def numberChangingPyramid(cls, rows):
        num = 1
        for i in range(0, rows):
            for j in range(0, i+1):
                print(num, end=' ')
                num += 1
            print()

    @classmethod
    def zeroOneTriangle(cls, rows):
        for i in range(0, rows):
            for j in range(0,i+1):
                if (i+j) % 2 == 0:
                    print(1,end=' ')
                else:
                    print(0,end=' ')
            print()


if __name__ == '__main__':
    pattern = Patterns()
    # pattern.hollowSquare(width=5,height=4)
    # pattern.numberIncreasingPyramid(rows=5)
    # pattern.numberIncreasingReversePyramid(5)
    # pattern.numberChangingPyramid(5)
    pattern.zeroOneTriangle(5)
    