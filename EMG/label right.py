import pandas as pd

# 读取Excel文件
file_path = 'rms right.xlsx'  # 请将此路径替换为你的Excel文件路径
df = pd.read_excel(file_path)

# 假设数据列为 'data1' 和 'data2'，创建标签列
df['label'] = df.apply(lambda row: 2 if row['Left RMS'] < 10 and row['Right RMS'] > 10 else 0, axis=1)

# 保存到新的Excel文件
output_file_path = 'label right.xlsx'  # 请将此路径替换为你希望保存的文件路径
df.to_excel(output_file_path, index=False)

print("标签已成功添加并保存到新的Excel文件中。")