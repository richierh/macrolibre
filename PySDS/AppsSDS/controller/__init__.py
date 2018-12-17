from AppsSDS import sds

class Controller(sds.):
    
    "Class ini digunakan untuk menampung data dari input Frame"
    
    def __init__(self,*args,**kwds):
        self.listdata = [2,3,4,5]
        
    
    def getdatapeserta(self):
        self.data =self.listdata
        return self.data
    
tes = Controller()
print (tes.getdatapeserta())