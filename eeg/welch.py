import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

who='ADHD'
data = data = pd.read_csv(f'./dataset/first/All_Remove_Noise_{who}_DataSet/v33p.csv')[['O1']]
'./add_label_ADHD_DataSet3/v15p.csv'
'./control_dataSet/v183p.csv'
data = data.transpose()

data = data.mean(0)  # Compute the mean signal across trials (the ERP).
print(data)
sns.set(font_scale=1.2)

# Define sampling frequency and time vector
sf = 128
time = np.arange(data.size) / sf

# Plot the signal
fig, ax = plt.subplots(1, 1, figsize=(12, 4))
plt.plot(time, data, lw=1.5, color='k')
plt.xlabel('Time (seconds)')
plt.ylabel('Voltage')

plt.xlim([time.min(), time.max()])
plt.title('N3 sleep EEG data (F3)')

sns.despine()
plt.show()
from scipy import signal

eeg_bands = {'Delta': (0.2, 4),  # 꿈없는 수면 상태에있을 때 뇌는 가장 느린 유형의 뇌파
             'Theta': (4, 8),  # 가볍게 잠을 자거나 극도로 긴장을 풀 때
             # alpah 특별히 어떤 것에 너무 집중하지 않을 때 이러한 파동을 생성
             # 무엇을하든 비교적 차분하고 편안하게 느껴질 것
             # 스트레스 수준을 낮추고 평온함을 느끼도록 도와주는 명상 및 휴식과 같은 활동에 반응
             'Alpha': (8, 12),  # 직감, 번득임, 문제해결, 기억력 집중력 최대 상태 // 긴장이 풀려 있으면서 의식집중이 이루어 있는 상태
             'SMR': (12, 15),  # 각성 상태, 가장 공부가 잘 되는 상태 //움직이지 않는 상태에서 집중력을 유지하는 상태
             'Beta': (15, 30),  # 크게 깨어 있고, 경계하고, 집중할때 일상 생활의 활동을하고 결정
             'Gamma': (30, 100)}  # 정보 처리 및 학습에 적극적으로 참여할 때 뇌는 가장 빠른 뇌파 인 감마 파를 생성
# Define window length (4 seconds)
win = 4 * sf
freqs, psd = signal.welch(data, sf, nperseg=win)
print(len(psd))
print(len(freqs))
eeg_range = {'Delta': np.logical_and(freqs >= eeg_bands['Delta'][0], freqs <= eeg_bands['Delta'][1]),
             'Theta': np.logical_and(freqs >= eeg_bands['Theta'][0], freqs <= eeg_bands['Theta'][1]),
             # alpah 특별히 어떤 것에 너무 집중하지 않을 때 이러한 파동을 생성
             # 무엇을하든 비교적 차분하고 편안하게 느껴질 것
             # 스트레스 수준을 낮추고 평온함을 느끼도록 도와주는 명상 및 휴식과 같은 활동에 반응
             'Alpha': np.logical_and(freqs >= eeg_bands['Alpha'][0], freqs <= eeg_bands['Alpha'][1]),
             'SMR': np.logical_and(freqs >= eeg_bands['Beta'][0], freqs <= eeg_bands['Beta'][1]),
             'Beta': np.logical_and(freqs >= eeg_bands['SMR'][0], freqs <= eeg_bands['SMR'][1]),
             'Gamma': np.logical_and(freqs >= eeg_bands['Gamma'][0], freqs <= eeg_bands['Gamma'][1])
             }
# Plot the power spectrum
sns.set(font_scale=1.2, style='white')
plt.figure(figsize=(8, 4))
plt.plot(freqs, psd, color='k', lw=2)
plt.fill_between(freqs, psd, where=eeg_range['Delta'], color='#FF33A3')
plt.fill_between(freqs, psd, where=eeg_range['Theta'], color="#EA33FF")
plt.fill_between(freqs, psd, where=eeg_range['Alpha'], color="#BC33FF")
plt.fill_between(freqs, psd, where=eeg_range['SMR'], color="#33A3FF")
plt.fill_between(freqs, psd, where=eeg_range['Beta'], color="#336DFF")
plt.fill_between(freqs, psd, where=eeg_range['Gamma'], color="#33FF69")
plt.xlabel('Frequency (Hz)')

#plt.ylim([0,3000])
plt.ylabel('Power spectral density (V^2 / Hz)')
#plt.yscale('log')

plt.title("Welch's periodogram")
plt.xlim([0, 48])
plt.grid(True)
sns.despine()
# Define delta lower and upper limits
plt.show()

from scipy.integrate import simps

# Frequency resolution
freq_res = freqs[1] - freqs[0]  # = 1 / 4 = 0.25
print(freq_res)
# Compute the absolute power by approximating the area under the curve

delta_power = simps(psd[eeg_range['Delta']], dx=freq_res)
print('Absolute delta power: %.3f uV^2' % delta_power)
delta_power = simps(psd[eeg_range['Theta']], dx=freq_res)
print('Absolute delta power: %.3f uV^2' % delta_power)
total_power = simps(psd, dx=freq_res)
print(total_power)
delta_rel_power = delta_power / total_power
print('Relative delta power: %.3f' % delta_rel_power)
