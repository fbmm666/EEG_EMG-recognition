import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 加载训练好的模型
clf = joblib.load('random_forest_model.pkl')

# 读取新数据及其真实标签
new_data_file = 'test.xlsx'
new_df = pd.read_excel(new_data_file)

# 提取特征数据和真实标签
X_new = new_df.iloc[:, 1:-1].values  # 特征数据（假设真实标签在最后一列）
y_true = new_df.iloc[:, -1].values   # 真实标签

# 使用模型进行预测
y_pred = clf.predict(X_new)

# 计算并打印准确率
accuracy = accuracy_score(y_true, y_pred)
print("新数据的准确率:", accuracy)

# 打印详细的分类报告和混淆矩阵
print("分类报告:\n", classification_report(y_true, y_pred))
print("混淆矩阵:\n", confusion_matrix(y_true, y_pred))
