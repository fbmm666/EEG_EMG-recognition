import pandas as pd
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import os

def read_emg_data(file_path):
    df = pd.read_excel(file_path)
    channel_1 = df.iloc[:, 0].values
    channel_2 = df.iloc[:, 1].values
    return channel_1, channel_2


def bandpass_filter(emg_signal, lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = signal.butter(order, [low, high], btype='band')
    y = signal.filtfilt(b, a, emg_signal)
    return y


def notch_filter(emg_signal, notch_freq, bandwidth, fs, order=4):
    nyquist = 0.5 * fs
    low = (notch_freq - bandwidth / 2) / nyquist
    high = (notch_freq + bandwidth / 2) / nyquist
    b, a = signal.butter(order, [low, high], btype='stop')
    y = signal.filtfilt(b, a, emg_signal)
    return y


def preprocess_emg_data(emg_signal, fs):
    # 去均值
    emg_signal = emg_signal - np.mean(emg_signal)
    # 带通滤波 (10-450 Hz)
    emg_signal = bandpass_filter(emg_signal, 10, 450, fs)
    # 陷波滤波 (去除工频噪声，假设为60 Hz)
    emg_signal = notch_filter(emg_signal, 60, 2, fs)

    return emg_signal


def plot_emg_signals(original_signal, filtered_signal, fs, title):
    t = np.arange(0, len(original_signal) / fs, 1 / fs)
    plt.figure(figsize=(12, 6))
    plt.plot(t, original_signal, label='Original Signal')
    plt.plot(t, filtered_signal, label='Filtered Signal', linestyle='--')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title(title)
    plt.legend()
    plt.show()


def main():
    file_path = r'D:\python\EMG\good right.xlsx'  # 替换为你的文件路径
    fs = 1500  # 采样率，替换为你的实际采样率

    channel_1, channel_2 = read_emg_data(file_path)

    filtered_channel_1 = preprocess_emg_data(channel_1, fs)
    filtered_channel_2 = preprocess_emg_data(channel_2, fs)

    plot_emg_signals(channel_1, filtered_channel_1, fs, 'Left EMG Signal')
    plot_emg_signals(channel_2, filtered_channel_2, fs, 'Right EMG Signal')

    # 如果需要将处理后的数据保存到新的Excel文件中
    filtered_df = pd.DataFrame({
        'Left': filtered_channel_1,
        'Right': filtered_channel_2
    })
    filtered_df.to_excel('filtered good right.xlsx', index=False)


if __name__ == "__main__":
    main()