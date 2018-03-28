from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../../../data/data.csv')
data = Counter(df['Eye Colour'])

colours = data.keys()
frequencies = list(data.values())
positions = list(range(len(colours)))

fig, ax = plt.subplots(1)

ax.bar(positions, frequencies, edgecolor='black',
       color=['darkorange', 'royalblue', 'green', 'gold', 'firebrick'])
ax.set_xticks(positions)
ax.set_xticklabels(colours)

fig.savefig('plot.png')
