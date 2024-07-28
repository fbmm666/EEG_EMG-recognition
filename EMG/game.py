from pynput.keyboard import Controller
import joblib
import numpy as np

# 加载模型和标准化器
clf = joblib.load('bio_model.pkl')
scaler = joblib.load('scaler.pkl')
keyboard = Controller()


def get_real_time_data():
    # 模拟获取实时数据(实时获取数据:1.使用设备的API或SDK 2.通过串口获取数据，代码实现 3.网络通信，类似wifi，代码实现)
    eeg_data = np.random.rand(1, 3)
    emg_data = np.random.rand(1, 3)
    return np.concatenate([eeg_data, emg_data], axis=1)


def control_game(prediction):
    if prediction == 0:
        keyboard.press('w')
        keyboard.release('w')
    elif prediction == 1:
        keyboard.press('a')
        keyboard.release('a')
    elif prediction == 2:
        keyboard.press('s')
        keyboard.release('s')
    elif prediction == 3:
        keyboard.press('d')
        keyboard.release('d')


def predict_and_control():
    while True:
        new_data = get_real_time_data()
        new_data_scaled = scaler.transform(new_data)
        prediction = clf.predict(new_data_scaled)
        control_game(prediction[0])

        import time
        time.sleep(1)


predict_and_control()
