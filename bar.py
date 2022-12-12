import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import squarify
from datetime import datetime
import csv
import numpy as np


fig, ax = plt.subplots(figsize=(22, 12))
# top 10 countries
countries = ["Australia", "Brazil", "China", "Mexico", "Namibia", "USA", "Russia", "Saudi Arabia"]
# total million tons 2016
pollution = [6.47, 45.1, 21.6, 14.2, 28.33, 26, 2, 18.9]


ax.bar(countries, pollution)
ax.set_xlabel("Country", fontsize=20,fontweight="bold")
ax.set_ylabel("Million Tons of Plastic Pollution (2016)", fontsize=20,fontweight="bold")
plt.rc('font', size=30)
plt.xticks(fontsize=20, rotation=45)
plt.yticks(fontsize=20)
plt.title("Plastics Waste Produced In 2016 (Million Tons)",fontsize=30,fontweight="bold")
plt.savefig('0.png')
plt.show()

