"""Inserting %20 in whitespaces"""

class Space_code:

    def replace_space(self,a):
        self.result = []
        self.abc = ""
        for i in a:
            if i.isspace() == True:
                self.result.append('%')
                self.result.append('2')
                self.result.append('0')
            else:
                self.result.append(i)
        for i in range(len(self.result)):
            self.abc += self.result[i]

        return self.abc

if __name__ == '__main__':
    a =  input()
    b = Space_code()
    print(b.replace_space(a))
    