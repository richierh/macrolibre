import itertools

import csv


class CustomPermutation(itertools.permutations):
    
    def __init__(self, *args, **kwds):
        super(CustomPermutation, self).__init__()
        self.result = args[0]
        self.__method()
        self.permutation = itertools.permutations(self.objectoflist)
        self.readpermutation()
    def __method(self):
        self.objectoflist = []
        for i in self.result.upper():
            self.objectoflist.append(i)
        print (self.objectoflist)       
        
    def insert(self):
        with open('permut.csv', 'w') as writeFile:
            write = csv.writer(writeFile)
            write.writerows([lista for lista in self.listformat])
        writeFile.close()
        
    def readpermutation(self):
        self.listcomp = [lista for lista in self.permutation]
        self.listformat = []
        for j in self.listcomp:
            self.listformat.append(["".join(j)])
        return self.listformat
    
 
if __name__ == "__main__":
    itter = ("karet")
    run = CustomPermutation(itter)
    run.insert()

