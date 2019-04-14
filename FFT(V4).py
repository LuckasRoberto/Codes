import csv
import pandas as pd
import numpy as np
from numpy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import numba as njit
import wave
import pylab
import scipy.signal
import scipy.io.wavfile

sampling_frequency, wav_data = scipy.io.wavfile.read('C:/Users/lucas/OneDrive/Área de Trabalho/IYPT/Star Wars/Audios/mola 4/wav/Mola 4- Angulo 40.wav')

def convert_wav_to_float(data):
    if data.dtype == np.int8:
        data = (data - 128) / 128.
    elif data.dtype == np.int16:
        data = data / 32768.
    elif data.dtype == np.int32:
        data = data / 2147483648.
    return data

wav_data = convert_wav_to_float(wav_data)

n_samples = len(wav_data)
total_duration = n_samples / sampling_frequency
sample_times = np.linspace(0, total_duration, n_samples)

plt.plot(sample_times, wav_data);

plt.ylabel('Amplitude')
plt.xlabel('Tempo(s)')
plt.show()

Y = np.fft.fft(wav_data)

X = np.linspace(0, sampling_frequency, n_samples)

plt.plot(X, np.abs(Y))
plt.ylabel('Amplitude')
plt.xlabel('Frequencia ($Hz$)')
plt.show()

