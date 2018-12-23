#!usr/bin/python
import os
import pathlib

import openpyxl

filename = pathlib.Path(os.getcwd() + "/AppsSDS/dataof.xlsx")
print (filename)

workexcel = openpyxl.load_workbook(filename, read_only=False, keep_vba=True, data_only=True, \
                        guess_types=False, keep_links=True)
workexcel.save(filename)
listprofesion = {}
listcell = 529
for i in range(listcell) :
    key = workexcel["Alphabetized Index"]["B1{}".format(i)].value
    value = workexcel["Alphabetized Index"]["D1{}".format(i)].value
    listprofesion.update({key:value})
    print (key)
print (listprofesion.keys())
# workexcel.get_named_range("Alphabetized Index")
