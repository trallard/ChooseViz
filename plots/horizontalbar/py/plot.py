from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../../../data/data.csv')
data = Counter(df['Eye Colour'])

colours = data.keys()
frequencies = list(data.values())
positions = list(range(len(colours)))

fig, ax = plt.subplots(1)

ax.barh(positions, frequencies, edgecolor='black',
        color=['darkorange', 'royalblue', 'green', 'gold', 'firebrick'])
ax.set_yticks(positions)
ax.set_yticklabels(colours)

fig.savefig('plot.png')
