#!/usr/bin/python
# -*- coding : utf-8 -*-

import os
import csv
import Tix
import matplotlib.pyplot as plt
from Tkinter import *
from tkMessageBox import *

# fonctions
# fonction qui montre le choix de chaque liste deroulante
def show_value():
	showinfo('Values', 
		  'The value for x is : ' + str(variable1.get()) + '\n'
		+ 'The value for y is : ' + str(variable2.get()) + '\n')

# fonction qui affiche le graphe
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
# FrameZ = Frame(l, borderwidth=2, relief=GROOVE)
# FrameZ.pack(side=LEFT, padx=30, pady=30)
FrameButton = Frame(l, borderwidth=2, relief=GROOVE)
FrameButton.pack(side=BOTTOM, padx=30, pady=30)

# Ajout de labels
Label(FrameX, text="Your X?").pack(padx=30, pady=30)
Label(FrameY, text="Your Y?").pack(padx=30, pady=30)
# Label(FrameZ, text="Your Z?").pack(padx=30, pady=30)
Label(FrameButton, text="Your doing?").pack(padx=30, pady=30)

# declaration et initalisation des variables
variable1 = IntVar(l)
variable2 = IntVar(l)
# variable3 = StringVar(l)
variable1.set(1) # default value
variable2.set(4) # default value
# variable3.set("seven") # default value

# valeurs dans les listes
x = OptionMenu(FrameX, variable1, 1, 2, 3)
x.pack()
y = OptionMenu(FrameY, variable2, 4, 5, 6)
y.pack()
# z = OptionMenu(FrameZ, variable3, "seven", "eight", "nine")
# z.pack()

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