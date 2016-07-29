#!/usr/bin/python
# -*- coding : utf-8 -*-

import os
import csv
import numpy as np
import Tix
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from Tkinter import *
from tkMessageBox import *
import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import sys
if sys.version_info[0] >= 3:
    import tkinter as tk
else:
    import Tkinter as tk

# fonctions
# fonction qui montre le choix de chaque liste deroulante
def show_value():
	showinfo('Values', 
		  'The value for x is : ' + str(variable1.get()) + '\n'
		+ 'The value for y is : ' + str(variable2.get()) + '\n')

# fonction qui affiche le graph
def show_graphe():
	plt.plot([variable1.get(), variable2.get()])
	plt.ylabel('some numbers')
	plt.show()

# declaration de la fenetre
fenetre = Tk()
fenetre['bg']='white'

# declaration et initialisation des frames
l = LabelFrame(fenetre, text="Print data into graph", padx=20, pady=20)
l.pack(fill="both", expand="yes")
FrameX = Frame(l, borderwidth=2, relief=GROOVE)
FrameX.pack(side=LEFT, padx=30, pady=30)
FrameY = Frame(l, borderwidth=2, relief=GROOVE)
FrameY.pack(side=LEFT, padx=30, pady=30)
FrameButton = Frame(l, borderwidth=2, relief=GROOVE)
FrameButton.pack(side=BOTTOM, padx=30, pady=30)

# Ajout de labels
Label(FrameX, text="Your first choice?").pack(padx=30, pady=30)
Label(FrameY, text="Your second choice?").pack(padx=30, pady=30)
Label(FrameButton, text="Your doing?").pack(padx=30, pady=30)

keylist = []

# Read file and put data into list
with open('example/choice.csv','r') as csvfile:
	reader = csv.reader(csvfile)
	plots = csv.reader(csvfile, delimiter=',')
	with open('coors_new.csv', mode='w') as outfile:
		writer = csv.writer(outfile)
		datachoice = dict((rows[0],rows[1:]) for rows in reader)

# Read file and put data into list
with open('example/sampleCSV.csv','r') as csvfile:
	reader = csv.reader(csvfile)
	plots = csv.reader(csvfile, delimiter=',')
	row1 = next(reader)   #gets the first line
	with open('coors_new.csv', mode='w') as outfile:
		writer = csv.writer(outfile)
		data = dict((rows[0],rows[1:]) for rows in reader)

# valeurs dans dict
for key in datachoice.keys():
	keylist += [str(key)]

# declaration et initalisation des variables
variable1 = StringVar(l)
variable2 = StringVar(l)
variable1.set("Choose you environement") # default value
variable2.set("Select the choice first") # default value

x = apply(OptionMenu, (FrameX, variable1) + tuple(keylist))
x.pack()

# boutons
# bouton pour afficher le choix de x, y, z
button = Button(FrameButton, text="See choice", command=show_value)
button.pack() 

# bouton pour afficher le graphe
button = Button(FrameButton, text="See graph", command=show_graphe)
button.pack() 

# bouton de sortie
bouton=Button(FrameButton, text="Close", command=l.quit)
bouton.pack()

mainloop()

