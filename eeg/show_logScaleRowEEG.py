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
# Plot it!
s=100

data2 = np.array([[data.loc['T7'][:s].values, data.loc['T8'][:s].values,data.loc['Pz'][:s].values],
                 [data.loc['T7'][s:s*2].values, data.loc['T8'][s:s*2].values,data.loc['Pz'][s:s*2].values],
                 [data.loc['T7'][s*2:s*3].values, data.loc['T8'][s*2:s*3].values,data.loc['Pz'][s*2:s*3].values],
                 [data.loc['T7'][s*3:s*4].values, data.loc['T8'][s*3:s*4].values,data.loc['Pz'][s*3:s*4].values],
                 [data.loc['T7'][s*4:s*5].values, data.loc['T8'][s*4:s*5].values,data.loc['Pz'][s*4:s*5].values]])

info = mne.create_info(ch_names, ch_types=['misc']*3, sfreq=sampling_freq)
info.set_montage('standard_1020')
events = np.column_stack((np.arange(0, 128*5, sampling_freq),
                          np.zeros(5, dtype=int),
                          np.array([1, 2, 1, 2, 1])))
print(events)
event_dict = dict(condition_A=1, condition_B=2)
simulated_epochs = mne.EpochsArray(data2, info,events=events,event_id=event_dict,tmin=-0.4)
simulated_epochs.plot(picks='misc',events=events,
                      event_id=event_dict)
plt.show()

info = mne.create_info(ch_names, ch_types=['eeg']*3, sfreq=sampling_freq)
raw = mne.io.RawArray(data.values, info)
print(data)
ica = mne.preprocessing.ICA(n_components=3, random_state=97, max_iter=800)
ica.fit(raw)
ica.plot_properties(raw)
plt.show()



