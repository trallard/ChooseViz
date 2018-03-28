import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('../../../data/data.csv')

fig, ax = plt.subplots(1)
ax.hist(data['Height'],
        bins=[150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210],
        color='darkorange',
        edgecolor='black',
        alpha=0.5)
fig.savefig('plot.png')