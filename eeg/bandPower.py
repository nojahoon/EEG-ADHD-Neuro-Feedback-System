import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
from pylab import *
import yasa
import os

if __name__ == '__main__':
    pd.set_option('display.max_row', 500)
    pd.set_option('display.max_columns', 100)
    q = []

    fs = 128  # Sampling rate (512 Hz)
    who = 'ADHD'
    file = f'dataset/{who}_band_power'
    sensor = ['Fp1', 'Fp2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7',
              'F8', 'T7', 'T8', 'P7', 'P8', 'Fz', 'Cz', 'Pz']
    
    path = f'./dataset/All_Remove_Noise_{who}_DataSet/'
    feature = [path + i for i in os.listdir(path)]
    try:
        os.mkdir(file)
    except:
        pass
    for i, ad in enumerate(feature):
        try:
            sf = 128
            data = pd.read_csv(ad)
            data=data/10
    
            data = data.transpose()
    
            # freqs, psd = signal.welch(adhd_data, sf, nperseg=win)
            a = yasa.bandpower(data.values, sf=sf, ch_names=sensor, relative=False)
            print(a)
            #a.loc[:, :'Gamma'].to_csv(f'./{file}/{who}_{i}.csv')
            """
            plt.bar(x=a.loc['T7', :'Gamma'].index, height=a.loc['T7', :'Gamma'])
            plt.show()
            plt.bar(x=c.loc['T7', :'Gamma'].index, height=a.loc['T7', :'Gamma'])
            plt.show()
            """
    
        except FileNotFoundError:
            pass
        else:
            pass
        """
    y=[adhd_data.index]*6
    x=[[i]*len(a.columns[:6]) for i in a.columns[:6]]
    print(x)
    print(y)
    print(q)
    pcolormesh(x,y,q, cmap='jet')  # Plot the result
    colorbar()  # ... with a color bar,
    
    xlabel('Time [s]')  # ... and label the axes
    ylabel('Frequency [Hz]')
    show()
    import pandas
    """
