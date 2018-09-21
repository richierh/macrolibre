import os
import subprocess
from string import ascii_lowercase

def convertingvol():
    text = "4036E49C"
    #print (text.split()[0][2])
    text = text.lower()
    #print (len(text))
    c =[]
    for i in range(len(text)):
        a = text.split()[0][i]
        #print (text.split()[0][i])
        
        char = ord(a)
    
        c.append(char*43)
        c.append("-")
        #print (c)
        ka = "".join(map(str,c))
    return ka[:-1]

#print (convertingvol())



def convertingnumtovol():

    pass


# Get the ASCII number of a character
'''number = ord(text)
'print (number)
'''
# Get the character given by an ASCII number
'''char = chr(number)
'''
class RunProgram():

    def __init__(self):
        simplecurrentdir = os.path.dirname(os.path.abspath(__file__))
        LibreOfficePortable = "\AplikasiBinaKarir\LibreOfficePortable.exe"
        FileLocation = "\AplikasiBinaKarir\AplikasiSDS.ods "
       # MacroLocation2 = "macro:///Hexacode.CoreHexa.main()"
       # MacroLocation = "macro:///Hexacode.CoreHexa.passwordopendoc()"
        Norestore = "--norestore"
        Nologo = "--nologo"
        Nodefault ="--nodefault"
        path = ("{} {} {} {} {}"\
        .format(simplecurrentdir+LibreOfficePortable,simplecurrentdir+FileLocation\
        ,Norestore,Nologo,Nodefault))
        print (path)
        print (os.path.dirname(os.path.abspath(__file__)))

        cmd = path
        subprocess.Popen(cmd)

class HardwareId():

    def __init__(self):
        self.data = os.popen('vol '+'c:', 'r').read()
        self.data = self.data.split()
        self.volume=self.data[len(self.data)-1:]
        self.volumeid=str(self.volume[0])
        self.code = str(self.volumeid)
        self.code = str(self.code.replace("-",""))
        print (self.code)

    def executecondition(self):
        
        if self.code== "4036E49C":
            self.result =  "Tsrue"
        else:
            self.result = "False"
        return self.result
'''
LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 

def alphabet_position(text):
    text = text.lower()

    numbers = [LETTERS[character] for character in text if character in LETTERS]

    return ' '.join(numbers*5)

print (alphabet_position(text))
'''
if __name__=="__main__":
    check = HardwareId()
   
    check = check.executecondition()
    RunApp = RunProgram()
    if check == "True":
        print ("RunApps")
        RunApp = RunProgram()

    else :
        print ("False")
        raise SystemExit()
    #RunApps=RunProgram(None)
    #raise SystemExit
 