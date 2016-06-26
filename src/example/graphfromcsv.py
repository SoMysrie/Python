#!/usr/bin/python
# -*- coding : utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.colorbar
import matplotlib.collections as collections
import matplotlib.backend_bases as backend_bases
import matplotlib.widgets as widgets
from mlab import dist
import csv

def graph():
	date, value = np.loadtxt('sampleCSV.csv', delimeter=',', unpack=True,converters = {0:mdates.strpdate2num('%Y-%m-%d')})
	fig = plt.figure()
	axl = fig.add_subplot(1,1,1, axisbg='white')
	plt.plot_date(x=date, y=value, fmt='-')
	plt.title('title')
	plt.ylabel('value')
	plt.xlabel('date')
	plt.show()

graph()
