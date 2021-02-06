import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
import random
import os
import seaborn as sns
from pylab import *

f = 'dataset/all_bandpower/all_dataset.csv'
all_data = pd.read_csv(f, index_col='Unnamed: 0')
target=all_data['result']
all_data=all_data.loc[:,'T8_Delta':'T8_Gamma']
all_data['result']=target
g = sns.pairplot(log(all_data), hue='result')
g.map(plt.scatter, s=15, edgecolor="w");
# diagonal
# lower
g.map_lower(plt.scatter, s=15, edgecolor="w")
g.map_lower(sns.regplot, scatter=False, truncate=False, ci=False)

g._legend.remove()
g.add_legend(title='', frameon=True)

for i, d in enumerate(['adhd', 'control']):
    g._legend.texts[i].set_text(d)

plt.show()
# plt.savefig(f'./{file}/{who}_{q}.png')
plt.close()
