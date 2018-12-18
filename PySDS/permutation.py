import itertools

import csv

class CustomPermutation(itertools.permutations):
    
    def __init__(self,*args,**kwds):
        super(CustomPermutation,self).__init__()#,**kwds)
        self.objectoflist=str(args[0]).upper()
        self.permutation=itertools.permutations(self.objectoflist)
    
    def insert(self):
        with open('permut.csv', 'w') as writeFile:
            write = csv.writer(writeFile)
            write.writerows([lista for lista in self.k])
        writeFile.close()
        
    def readpermutation(self):
        a = [lista for lista in self.permutation]
        self.k = []
        for j in a:
            self.k.append(["".join(j)])
        return self.k
    
 
if __name__=="__main__":
    itter = ("r","e","c")
    run = CustomPermutation(itter)
    run.readpermutation()
    run.insert()

