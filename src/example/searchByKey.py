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


# Read file and put data into list
with open('sampleCSV.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    plots = csv.reader(csvfile, delimiter=',')
    xVal = next(reader)   #gets the first line
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        yVal = dict((rows[0],rows[1:]) for rows in reader)


search_key = raw_input("Provide key")
for key, news in yVal.iteritems():
    if key == search_key:
        print news