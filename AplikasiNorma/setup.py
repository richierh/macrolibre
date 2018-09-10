import os
data = os.popen('vol '+'c:', 'r').read()
data = data.split()
volume=data[len(data)-1:]
volumeid=str(volume[0])
code = str(volumeid)
code = str(code.replace("-",""))
print (code)

if code== "4036E49C":
    print ("True")
else:
    print ("false")
