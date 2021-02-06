from scipy.io import loadmat  # To load .mat files
from pylab import *  # Import plotting functions
from IPython.lib.display import YouTubeVideo
from numpy import where
from numpy.fft import fft, rfft
from scipy.signal import spectrogram
import pandas as pd

rcParams['figure.figsize'] = (12, 3)

data = data = pd.read_csv('./dataset/first/Remove_Noise_Control_DataSet/v204p.csv')[['Pz']]
EEG = data
sf = 128
t = np.arange(EEG.size) / sf

x = EEG  # Relabel the data variable
dt = t[1] - t[0]  # Define the sampling interval
N = x.shape[0]  # Define the total number of data points
T = N * dt  # Define the total duration of the data

xf = fft(x - x.mean())  # Compute Fourier transform of x
Sxx = 2 * dt ** 2 / T * (xf * xf.conj())  # Compute spectrum
Sxx = Sxx[:int(len(x) / 2)]  # Ignore negative frequencies

df = 1 / T.max()  # Determine frequency resolution
fNQ = 1 / dt / 2  # Determine Nyquist frequency
faxis = arange(0, fNQ, df)  # Construct frequency axis
"""
plot(faxis, Sxx.real)                 # Plot spectrum vs frequency
xlim([0, 100])                        # Select frequency range
xlabel('Frequency [Hz]')              # Label the axes
ylabel('Power [$\mu V^2$/Hz]')
show()
plot(t[:25], EEG[:25], 'o-')    # Plot the first 25 points of data,
xlabel('Time [s]')              # ... with axes labeled.
ylabel('Voltage [$\mu V$]')
show()
lags = arange(-len(x) + 1, len(x))    # Compute the lags for the full autocovariance vector
                                      # ... and the autocov for L +/- 100 indices
ac = 1 / N * correlate(x - x.mean(), x - x.mean(), mode='full')
inds = abs(lags) <= 100               # Find the lags that are within 100 time steps
plot(lags[inds] * dt, ac[inds])       # ... and plot them
xlabel('Lag [s]')                     # ... with axes labelled
ylabel('Autocovariance')
show()
inds = range(100)          # Choose a subset of the data to plot
plot(t[0:100], x[0:100], label="original");   # Plot the original
L=0;                       # Choose the lag,
                           # ... and plot the shifted traces.
plot(t[inds], x[[i + L for i in inds]], '--',
     label="L={}".format(L))
legend(loc='upper right')  # Add a legend and informative title
title("Original time series data, and shifted by amount L\nAutocovariance = {:.4}".format(ac[lags==L][0]));

ac[lags == 0]
L=int(2*1/60/dt);                               # Choose the lag,
                                                # ... and plot the shifted traces.
plot(t[inds], x[[i + L for i in inds]], '--',
     label="L={}".format(L))
legend()                                        # Add a legend and informative title
title("Original time series data, and shifted by amount L\nAutocovariance = {:.4}".format(ac[lags==L][0]));
show()

xf = fft(x - x.mean())                  # Compute Fourier transform of x
Sxx = 2 * dt ** 2 / T * (xf * conj(xf)) # Compute spectrum
Sxx = Sxx[:int(len(x) / 2)]             # Ignore negative frequencies

df = 1 / T.max()                        # Determine frequency resolution
fNQ = 1 / dt / 2                        # Determine Nyquist frequency
faxis = arange(0,fNQ,df)                # Construct frequency axis

plot(faxis, real(Sxx))                  # Plot spectrum vs frequency
xlim([0, 100])                          # Select frequency range
xlabel('Frequency [Hz]')                # Label the axes
ylabel('Power [$\mu V^2$/Hz]')
show()

xf = rfft(x - x.mean()).real
Sxx = 2 * dt ** 2 / T * xf * xf.conj()
plot(Sxx)
xlabel('Indices')
ylabel('Power [$\mu V^2$/Hz]');
show()
"""
EEG = EEG.transpose()

mn = EEG.mean(0)  # Compute the mean signal across trials (the ERP).

Fs = 1 / dt  # Define the sampling frequency,
interval = int(Fs)  # ... the interval size,
overlap = int(Fs * 0.95)  # ... and the overlap intervals
print(Fs)
# Compute the spectrogram
f, t, Sxx = spectrogram(
    mn,  # Provide the signal,
    fs=Fs,  # ... the sampling frequency,
    nperseg=interval,  # ... the length of a segment,
    noverlap=overlap)  # ... the number of samples to overlap,

pcolormesh(t, f, 10 * log10(Sxx),
           cmap='jet')  # Plot the result
colorbar()  # ... with a color bar,

xlabel('Time [s]')  # ... and label the axes
ylabel('Frequency [Hz]')
show()


def spectrogram(self):
    print("Generating spectrogram...")
    f_lim_Hz = [0, 50]  # frequency limits for plotting
    plt.figure(figsize=(10, 5))
    ax = plt.subplot(1, 1, 1)
    plt.pcolor(self.spec_t, self.spec_freqs, 10 * np.log10(self.spec_PSDperBin))  # dB re: 1 uV
    plt.clim([-25, 26])
    plt.xlim(self.spec_t[0], self.spec_t[-1] + 1)
    plt.ylim(f_lim_Hz)
    plt.xlabel('Time (sec)')
    plt.ylabel('Frequency (Hz)')
    plt.title(self.plot_title('Spectrogram'))
    # add annotation for FFT Parameters
    ax.text(0.025, 0.95,
            "NFFT = " + str(self.NFFT) + "\nfs = " + str(int(self.fs_Hz)) + " Hz",
            transform=ax.transAxes,
            verticalalignment='top',
            horizontalalignment='left',
            backgroundcolor='w')
    self.plotit(plt, self.plot_filename('Spectrogram'))
