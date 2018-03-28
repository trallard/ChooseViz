from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../../../data/data.csv')
data = Counter(df['Eye Colour'])

colours = data.keys()
frequencies = list(data.values())
positions = list(range(len(colours)))

palette = ['darkorange', 'royalblue', 'green', 'gold', 'firebrick']

fig, ax = plt.subplots(1)

bottom = 0
for i, (freq, colour) in enumerate(zip(frequencies, colours)):

    # Adding the bar to be stacked
    ax.bar(0, freq, edgecolor='black', width=1,
           color=palette[i], bottom=bottom)

    # Adding a label in the middle of the bar
    y = bottom + freq / 2
    ax.text(0, y, colour, ha='center', va='center')

    bottom += freq

ax.set_xlim(-1, 1)
ax.set_xticks([])

fig.savefig('plot.png')
