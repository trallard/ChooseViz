import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import gaussian_kde

data = pd.read_csv('../../../data/data.csv')
density = gaussian_kde(data['Height'])

steps = 200
xs = np.linspace(data['Height'].min(), data['Height'].max(), steps)

fig, ax = plt.subplots(1)
ax.plot(xs, density(xs))
ax.fill_between(xs, [0]*steps, density(xs), alpha=0.3)
fig.savefig('plot.png')