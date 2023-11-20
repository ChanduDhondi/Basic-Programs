""" Here we are calculating the Triple sum of given Numbers with differenct Time Complexity """

class Triplet:

    def __init__(self,arr,s):
        self.arr = arr
        self.s = s
    
    def logic1(self):
        # Time complexity is O(N.N.N)
        self.result = []
        for i in range(len(self.arr)):
            for j in range(i+1,len(self.arr)):
                for k in range(j+1,len(self.arr)):
                    if self.arr[i] + self.arr[j] + self.arr[k] == self.s:
                        self.result.append((self.arr[i],
                                            self.arr[j],
                                            self.arr[k]))
        return self.result
    
    def logic2(self):
        # Two pointer approach 
        # Time Complexity is O(N.N)
        self.len = len(arr)
        self.result = []
        for i in range(len(self.arr[:-2])):
            j = i + 1 
            k = self.len - 1
            while j<k:
                if self.arr[i]+self.arr[j]+self.arr[k] == self.s:
                    self.result.append((self.arr[i],
                                        self.arr[j],
                                        self.arr[k]))
                    j += 1
                    k -= 1
                elif self.arr[i]+self.arr[j]+self.arr[k] > self.s:
                    k -= 1
                else:
                    j += 1

        return self.result

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8]
    s = 10
    triplet = Triplet(arr,s)
    print(triplet.logic1())
    print(triplet.logic2())
