#!/usr/bin/python
# -*- coding : utf-8 -*-f

name1 = "donnees/API_6_DS2_fr_csv_v2.csv"
file = open(fname1, "r")

try:
    reader = csv.reader(file)
    for row in reader:
		if row:
			print row[0],row[2]
finally:
	file.close() 