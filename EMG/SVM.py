import joblib  # 用于保存和加载模型
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 读取数据
file_path = 'test.xlsx'
df = pd.read_excel(file_path)

# 提取特征和标签
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# 数据集分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 创建并训练模型
# 创建SVM模型
clf = SVC(kernel='rbf', random_state=42)  # 使用非线性核(径向基)

# 训练模型
clf.fit(X_train, y_train)


# 保存模型
joblib.dump(clf, 'svm_model.pkl')

# 测试模型
y_pred = clf.predict(X_test)
print("测试集准确率:", accuracy_score(y_test, y_pred))
