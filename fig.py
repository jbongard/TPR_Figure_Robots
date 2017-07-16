import matplotlib.pyplot as plt
import pandas as pd
from urllib2 import urlopen
import numpy as np

csv = pd.read_csv("data.csv", index_col=0)
csv = csv.transpose()

csv.plot.bar(stacked=True)
plt.title('Number of robots in each species')
plt.xlabel('Day')
plt.ylabel('Population size')

plt.show()
