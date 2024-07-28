import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def calculate_rms(signal):
    """
    计算 RMS 特征
    :param signal: 输入信号 (numpy array)
    :return: RMS 特征值 (float)
    """
    return np.sqrt(np.mean(signal ** 2))


def extract_rms_features_from_excel(file_path, frame_size, step_size):
    """
    从 Excel 文件中提取 RMS 特征
    :param file_path: Excel 文件路径 (string)
    :param frame_size: 窗口大小 (样本数)
    :param step_size: 步长 (样本数)
    :return: 包含 RMS 特征值的 DataFrame
    """
    # 读取 Excel 文件
    df = pd.read_excel(file_path)

    # 提取信号数据
    channel_1 = df['Left'].values
    channel_2 = df['Right'].values

    # 提取特征
    features_channel_1 = []
    features_channel_2 = []
    times = []

    for start in range(0, len(channel_1) - frame_size + 1, step_size):
        end = start + frame_size
        segment_1 = channel_1[start:end]
        segment_2 = channel_2[start:end]

        rms_value_1 = calculate_rms(segment_1)
        rms_value_2 = calculate_rms(segment_2)

        features_channel_1.append(rms_value_1)
        features_channel_2.append(rms_value_2)

        times.append(start)

    # 创建 DataFrame
    features_df = pd.DataFrame({
        'Time': times,
        'Left RMS': features_channel_1,
        'Right RMS': features_channel_2
    })

    return features_df


def plot_rms_features(features_df):
    """
    绘制 RMS 特征的时间图
    :param features_df: 包含 RMS 特征值的 DataFrame
    """
    plt.figure(figsize=(12, 6))
    plt.plot(features_df['Time'], features_df['Left RMS'], label='Left RMS')
    plt.plot(features_df['Time'], features_df['Right RMS'], label='Right RMS')
    plt.xlabel('Time (samples)')
    plt.ylabel('RMS Value')
    plt.title('RMS Features Over Time')
    plt.legend()
    plt.show()



file_path = r'D:\python\EMG\filtered good right.xlsx'
frame_size = 100  # 窗口大小
step_size = 1  # 步长

# 提取特征
features_df = extract_rms_features_from_excel(file_path, frame_size, step_size)

# 保存到新的 Excel 文件
output_file_path = 'rms right.xlsx'
features_df.to_excel(output_file_path, index=False)

print(f'特征数据已保存到 {output_file_path}')

# 绘制 RMS 特征的时间图
plot_rms_features(features_df)
