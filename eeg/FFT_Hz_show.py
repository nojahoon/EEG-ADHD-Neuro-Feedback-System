import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings

fs = 128  # Sampling rate (128 Hz)

# Define EEG bands
eeg_bands = {'Delta': (0.2, 4),  # 꿈없는 수면 상태에있을 때 뇌는 가장 느린 유형의 뇌파
             'Theta': (4, 8),  # 가볍게 잠을 자거나 극도로 긴장을 풀 때
             # alpah 특별히 어떤 것에 너무 집중하지 않을 때 이러한 파동을 생성
             # 무엇을하든 비교적 차분하고 편안하게 느껴질 것
             # 스트레스 수준을 낮추고 평온함을 느끼도록 도와주는 명상 및 휴식과 같은 활동에 반응
             'Alpha': (8, 12),  # 직감, 번득임, 문제해결, 기억력 집중력 최대 상태 // 긴장이 풀려 있으면서 의식집중이 이루어 있는 상태
             'SMR': (12, 15),  # 각성 상태, 가장 공부가 잘 되는 상태 //움직이지 않는 상태에서 집중력을 유지하는 상태
             'Beta': (15, 30),  # 크게 깨어 있고, 경계하고, 집중할때 일상 생활의 활동을하고 결정
             'Gamma': (30, 48)}  # 정보 처리 및 학습에 적극적으로 참여할 때 뇌는 가장 빠른 뇌파 인 감마 파를 생성

data = pd.read_csv('./dataset/first/All_Remove_Noise_Control_DataSet/v41p.csv')[['Pz']]
# Get real amplitudes of FFT (only in postive frequencies)

eeg_band_fft = dict()

fft_vals = np.fft.rfft(data['Pz'])
fft_vals=np.delete(fft_vals,0)
# Get frequencies for amplitudes in Hz
fft_freq = np.fft.rfftfreq(len(data['Pz']), 1.0 / fs)

fft_freq=np.delete(fft_freq,0)

a = []
eeg_band_fft = dict()
all=[]
for band in eeg_bands:
    freq_ix, *_ = np.where((fft_freq >= eeg_bands[band][0]) &
                           (fft_freq < eeg_bands[band][1]))
    a.append(freq_ix)

    eeg_band_fft[band] = fft_vals[freq_ix]
    all.extend(fft_vals[freq_ix])

print(type(fft_vals))

# Plot the data (using pandas here cause it's easy)
import pandas as pd
pd.set_option('display.max_row', 1000)
pd.set_option('display.max_columns', 1000)

print(len(all))

ax = plt.subplot(3, 3, (1, 3))
ax.plot(range(len(data)), data)
ax.grid(True)
ax.set_xlabel('T7')
ax.set_ylabel("Values")


for (i, band), values in zip(enumerate(eeg_bands.keys(), start=4), eeg_bands.values()):
    ax = plt.subplot(3, 3, i)
    print(band)
    print(len(eeg_band_fft[band]))
    ax.plot(a[i - 4], eeg_band_fft[band])
    ax.grid(True)
    ax.set_xlabel(f'{band} {values[0]}~{values[1]}Hz')
    ax.set_ylabel("FFT")


"""plt.legend(
            labels=eeg_band_fft.keys(),  # The labels for each line
            loc="center right",  # Position of legend
            borderaxespad=0.1,  # Small spacing around legend box
            title="Legend Title"  # Title for the legend
        )
"""
plt.tight_layout()
plt.show()
