#!usr/bin/env python

import csv


class csvfile():

	def __init__(self):
		self.file = 'tk.py'
		pass
	
	
		
	def read(self):
		with open("tk.py", 'r') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
			for row in spamreader:
				l = ', '.join(row)
				print (l)
		return l


if __name__=="__main__":
	k = csvfile()
	k.read()
			