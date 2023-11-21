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
        self.arr1 = []
        self.result = []
        for i in range(len(arr)):
            self.diff= self.s-self.arr[i]
            if self.diff in self.arr1:
                self.result.append((arr[i],self.diff))                           
            self.arr1.append(arr[i])
        return self.result
    
    def logic3(self):
        # Using list.pop()
        # Time complexity is O(N)
        self.result = []
        for i in range(len(self.arr)):
            self.num = self.arr.pop()
            self.diff = self.s - self.num
            if self.diff in self.arr:
                self.result.append((self.diff,self.num))            
        return self.result 
                
if __name__ == '__main__':
    arr = [1,3,4,3,2,5]
    s = 6
    pairsum = PairSum(arr,s)
    print(pairsum.logic1())
    print(pairsum.logic2())
    print(pairsum.logic3())

  