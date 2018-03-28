from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../../../data/data.csv')
eye_colours = Counter(df['Eye Colour'])

fig, ax = plt.subplots(1)
ax.pie(eye_colours.values(),
       labels=eye_colours.keys(),
       explode=[0, 0, 0.2, 0, 0.1],
       shadow=True,
       colors=['darkorange', 'royalblue', 'green', 'gold', 'firebrick'])

fig.savefig('plot.png')
