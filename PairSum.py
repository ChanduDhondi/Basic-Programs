# Here we are calculating the Pair Sum of the given Numbers with different Time Complexity

class PairSum:

    def __init__(self,arr,s):
        self.arr = arr
        self.s = s
    
    def logic1(self):
        # Time complexity is O(N.N)
        self.result = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] + arr[j] == self.s:
                    self.result.append((arr[i],arr[j]))
        return self.result
    
    def logic2(self):
        # Time Complexity is O(N)
        self.result = []
        for i in range(len(arr)):
            self.num = arr.pop()
            self.diff= self.s-self.num
            if self.diff in self.arr:
                self.result.append((self.diff,self.num))
        return self.result
                     
if __name__ == '__main__':
    arr = [1,5,2,7,11,4,9]
    s = 9
    pairsum = PairSum(arr,s)
    print(pairsum.logic1())
    print(pairsum.logic2())

  