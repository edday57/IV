import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import squarify
from datetime import datetime
import csv
import numpy as np
file=open('d3.csv',encoding='utf-16')
csvreader=csv.reader(file,delimiter="\t")
names=[]
costs=[]
for row in csvreader:
        names.append(row[0])
        costs.append(float(row[1]))

fig, ax = plt.subplots(figsize=(12, 8))
# top 10 countries
countries = ["Africa", "Brazil", "China", "France", "India", "Japan", "Mexico", "Russia", "USA"]
# total million tons 2016
pollution = [6.47, 10.68, 21.6, 6.68, 26.33, 4.8, 5.9, 9.13, 34.02]


ax.bar(countries, pollution)
ax.set_xlabel("Country")
ax.set_ylabel("Tons of Plastic Pollution (2016)")
plt.rc('font', size=11)
plt.title("Plastic Pollution Per Country",fontsize=11,fontweight="bold")
plt.savefig('0.png')
plt.show()

