# Finding the longest Chain/Consequetive numbers in the given array

class LongestChain:

    def Logic1(self,arr):
        self.lenght = 1
        for i in range(len(arr)):
            if arr[i]-1 in arr:
                continue
            else:
                self.count = 1
                self.next_num = arr[i]+1 
                while self.next_num in arr:
                    self.next_num += 1
                    self.count += 1
                if self.count > self.lenght:
                    self.lenght = self.count
        return self.lenght
    
if __name__ == '__main__':
    arr = [9,0,3,6,2,4,7,8,13,10,11]
    chain = LongestChain()
    print(chain.Logic1(arr))