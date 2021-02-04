import numpy as np
import mne
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('./dataset/first/All_Remove_Noise_Control_DataSet/v41p.csv')

# Some information about the channels
ch_names = ['Fp1', 'Fp2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7',
            'F8', 'T7', 'T8', 'P7', 'P8', 'Fz', 'Cz', 'Pz']   # TODO: finish this list
ch_types = ['misc']*len(ch_names)

# Read the CSV file as a NumPy array
n_channels = 3
sampling_freq = 128  # in Hertz

info = mne.create_info(ch_names, ch_types=ch_types, sfreq=sampling_freq)
info.set_montage('standard_1020')

data = data.transpose()
raw = mne.io.RawArray(data.values, info)
raw.plot_psd(fmax=50,picks='misc')

plt.show()
