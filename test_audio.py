import numpy as np
import soundfile as sf

# 生成一个简单的音频信号
duration = 10  # 持续时间（秒）
sample_rate = 44100  # 采样率
t = np.linspace(0, duration, int(sample_rate * duration))

# 生成一个包含多个频率的信号
frequencies = [440, 880, 1320]  # A4, A5, E6
signal = np.zeros_like(t)
for f in frequencies:
    signal += np.sin(2 * np.pi * f * t)

# 添加一些振幅变化
envelope = np.ones_like(t)
envelope[:int(0.1 * sample_rate)] = np.linspace(0, 1, int(0.1 * sample_rate))  # 淡入
envelope[-int(0.1 * sample_rate):] = np.linspace(1, 0, int(0.1 * sample_rate))  # 淡出

signal *= envelope
signal /= np.max(np.abs(signal))  # 归一化

# 保存为 WAV 文件
output_path = 'test_music.wav'
sf.write(output_path, signal, sample_rate)
print(f"已生成测试音频文件: {output_path}") 