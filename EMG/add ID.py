import pandas as pd

# 读取特征值和标签数据
features_file_path = r'D:\python\EMG\rms_features.xlsx'
labels_file_path = r'D:\python\EMG\emg_label_right.xlsx'

df_features = pd.read_excel(features_file_path)
df_labels = pd.read_excel(labels_file_path)

# 为特征值和标签数据添加 ID 列
df_features['ID'] = range(1, len(df_features) + 1)
df_labels['ID'] = range(1, len(df_labels) + 1)

# 保存更新后的 Excel 文件
df_features.to_excel('features_with_id.xlsx', index=False)
df_labels.to_excel('emg_label_right_id.xlsx', index=False)

print("ID 列已成功添加到 Excel 文件中。")
