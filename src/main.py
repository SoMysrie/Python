#!/usr/bin/python
# -*- coding : utf-8 -*-

import os
import csv
import Tix
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from Tkinter import *
from tkMessageBox import *
import pandas as pd
import numpy as np
import sys
if sys.version_info[0] >= 3:
    import tkinter as tk
else:
    import Tkinter as tk


class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, allVal= None, xVal = None, yVal = None, search_key = None)
        # declaration et initialisation des frames
        l = tk.LabelFrame(self, text="Print data into graph", padx=20, pady=20)
        l.pack(fill="both", expand="yes")
        FrameChoice = Frame(l, borderwidth=2, relief=GROOVE)
        FrameChoice.pack(side=LEFT, padx=30, pady=30)
        FrameButton = Frame(l, borderwidth=2, relief=GROOVE)
        FrameButton.pack(side=BOTTOM, padx=30, pady=30)

        # Ajout de labels
        Label(FrameChoice, text="Your choice?").pack(padx=30, pady=30)
        Label(FrameButton, text="Your doing?").pack(padx=30, pady=30)

        # Read file and put data into list
        with open('donnees/choice.csv','r') as csvfile:
            reader = csv.reader(csvfile)
            plots = csv.reader(csvfile, delimiter=',')
            with open('coors_new.csv', mode='w') as outfile:
                writer = csv.writer(outfile)
                self.dict = dict((rows[0],rows[1:]) for rows in reader)

        # Read file and put data into list
        with open('donnees/sampleCSV.csv','r') as csvfile:
            reader = csv.reader(csvfile)
            plots = csv.reader(csvfile, delimiter=',')
            self.xVal = next(reader)   #gets the first line
            with open('coors_new.csv', mode='w') as outfile:
                writer = csv.writer(outfile)
                self.allVal = dict((rows[0],rows[1:]) for rows in reader)
        
        self.yVal = []
        
        self.variable_a = tk.StringVar(self)
        self.variable_b = tk.StringVar(self)

        self.variable_a.trace('w', self.update_options)

        self.optionmenu_a = tk.OptionMenu(FrameChoice, self.variable_a, *self.dict.keys())
        self.optionmenu_b = tk.OptionMenu(FrameChoice, self.variable_b, '')

        self.variable_a.set('')

        self.optionmenu_a.pack()
        self.optionmenu_b.pack()
        self.pack()

        # boutons
        # bouton pour afficher le choix
        button = Button(FrameButton, text="See choice", command=self.show_value)
        button.pack() 

        # bouton pour afficher le graphe
        button = Button(FrameButton, text="See graph", command=self.show_graphe)
        button.pack() 

        # bouton de sortie
        bouton=Button(FrameButton, text="Close", command=l.quit)
        bouton.pack()

    # fonctions
    # fonction qui montre le choix de chaque liste deroulante
    def show_value(self, *args):
        showinfo('Values', 
              'The first choice is  : ' + self.variable_a.get() + '\n'
            + 'The second choice is : ' + self.variable_b.get() + '\n')
    
    # fonction qui affiche le graph
    def show_graphe(self, *args):
        plt.plot([int(x) for x in self.xVal], [int(y) for y in self.yVal])
        plt.ylabel('some numbers') 
        plt.show()

    # fonction qui met a jour le choix
    def update_options(self, *args):
        informations = self.dict[self.variable_a.get()]
        self.variable_b.set(informations[0])

        menu = self.optionmenu_b['menu']
        menu.delete(0, 'end')

        for info in informations:
            menu.add_command(label=info, command=lambda infotype=info: self.variable_b.set(infotype))

        self.search_key = self.variable_b.get()
        self.variable_b.trace("w", self.callback)

        for key, news in self.allVal.iteritems():
            if key == self.search_key:
                self.yVal = news

    # fonction qui met a jour le 2eme choix
    def callback(self, *args):
        self.search_key = self.variable_b.get()
        for key, news in self.allVal.iteritems():
            if key == self.search_key:
                self.yVal = news

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.mainloop()