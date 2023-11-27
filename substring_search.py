"""Learning String Operations using OOP's"""

class String_search:
    
    def searching_substring(self,strg,sub_str):
        self.result = []
        if sub_str in strg:
            i = strg.find(sub_str)
            while i != -1:
                self.result.append(i)
                i = strg.find(sub_str,i+1)
            return self.result
        else:
            print('Given word in not there in String')
           
if __name__ == '__main__':
    strg = "I liked the movie, acting in movie was Great!"
    sub_str = "movie"
    a = String_search()
    print(a.searching_substring(strg,sub_str))
    