import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('../../../data/data.csv')

fig, ax = plt.subplots(1)
bp = ax.violinplot(data['Height'],
	               widths=0.4,
                   showmedians=True,
                   showextrema=True)
fig.savefig('plot.png')