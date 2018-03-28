import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('../../../data/data.csv')

fig, ax = plt.subplots(1)
bp = ax.boxplot(data['Height'],
	            whis=1.5,
	            showmeans=True)
fig.savefig('plot.png')