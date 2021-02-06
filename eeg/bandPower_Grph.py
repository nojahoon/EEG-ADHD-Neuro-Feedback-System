import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
import random
import os

who = 'Control'
sort_channel = 'Theta'
index = 0
sz_max = {'Delta': 300, 'Theta': 80, 'Alpha': 70, 'Sigma': 30, 'Beta': 15, 'Gamma': 5}
file = f'graph/{who}_bandpower'
path = f'./dataset/first/{who}_band_power_discriminant/'

try:
    os.mkdir(file)
except:
    pass
feature = [path + i for i in os.listdir(path)]
sensor = ['Fp1', 'Fp2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7',
          'F8', 'T7', 'T8', 'P7', 'P8', 'Fz', 'Cz', 'Pz']
hz=['Delta','Theta','Alpha','Sigma','Beta','Gamma']
for i, f in enumerate(feature):

        a = pd.read_csv(f, index_col='Unnamed: 0')
        title = a.columns
        q=title[0][:title[0].find('_')]
        a = a.rename(columns=dict(zip(title, sz_max.keys())))
        print(a)
        #a = a.loc[:,sort_channel:]
        #a = a.sort_values(by=sort_channel, ascending=False)
        a = a.loc[:, sort_channel:'Beta']
        print(a)

        c = plt.pcolormesh(a, cmap='jet', vmax=sz_max[sort_channel])  # Plot the result
        plt.colorbar()  # ... with a color bar,
        plt.title(q)
        plt.ylabel(f'Number of {who}')
        plt.xticks(range(1, len(a.columns) + 1), a.columns)  # x축 단위 바꾸기
        plt.show()
        #plt.savefig(f'./{file}/{who}_{q}.png')
        plt.close()
