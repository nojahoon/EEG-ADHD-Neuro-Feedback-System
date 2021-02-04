import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

who='Control'
path=f'./dataset/first/ratio2/Theta_Beta_ratio_Control_band_power/'
feature = [path + i for i in os.listdir(path)]
sns.set(font_scale=1.2)

who='ADHD'
path=f'./dataset/first/ratio2/Theta_Beta_ratio_ADHD_band_power/'
feature2 = [path + i for i in os.listdir(path)]

for f,f2 in zip(feature,feature2):
    print(f)
    q = f2[(f2.find(f'/{who}')):f2.find('.csv')][6:]
    df = pd.read_csv(f)
    print(df)
    df2= pd.read_csv(f2)
    print(f2)
    print(df2)
    # Plot the signal
    plt.scatter(range(len(df)), df, lw=1.5, color='k',)
    plt.scatter(range(len(df2)), df2, lw=1.5, color='r')
    plt.title(q)
    plt.legend(['control','adhd'])
    plt.show()
    plt.close()
