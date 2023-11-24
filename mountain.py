""" Here we are calculating the length of Biggest Mountain in Array"""

class Mountain:

    def logic(self,arr):
        self.arr = arr
        self.length = 0
        if len(self.arr) < 3:
            print("Please enter the array greater than size 3")
        else :
            for i in range(len(self.arr[1:-2])):
                self.count = 1
                if self.arr[i] > self.arr[i-1] and self.arr[i] > self.arr[i+1]:
                    j = i
                    # Backwards
                    while j>=1 and self.arr[j-1] <= self.arr[j]:
                        j -= 1 
                        self.count += 1 
                    # Forwards
                    while i<=len(self.arr)-2 and self.arr[i] >= self.arr[i+1]:
                        i += 1 
                        self.count += 1 
                self.length = max(self.count,self.length)

        return self.length            

if __name__ == '__main__':
    arr = [5,6,7,3,6,7,2,9,0,1,4,11,16,15,14,13,12]
    # arr = [1,2]
    length = Mountain()
    print(length.logic(arr))