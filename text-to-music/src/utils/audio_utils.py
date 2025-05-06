import soundfile as sf
import numpy as np
from pathlib import Path

def load_audio(file_path, sr=None):
    """
    加载音频文件
    :param file_path: 音频文件路径
    :param sr: 采样率，如果为None则使用原始采样率
    :return: 音频数据和采样率
    """
    audio, sample_rate = sf.read(file_path)
    if sr is not None and sr != sample_rate:
        # 这里可以添加重采样代码
        pass
    return audio, sample_rate

def save_audio(audio, file_path, sr):
    """
    保存音频文件
    :param audio: 音频数据
    :param file_path: 保存路径
    :param sr: 采样率
    """
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    sf.write(file_path, audio, sr)

def mix_audio(audio1, audio2, weights=(0.5, 0.5)):
    """
    混合两个音频
    :param audio1: 第一个音频数据
    :param audio2: 第二个音频数据
    :param weights: 混合权重
    :return: 混合后的音频
    """
    # 确保两个音频长度相同
    min_len = min(len(audio1), len(audio2))
    audio1 = audio1[:min_len]
    audio2 = audio2[:min_len]
    
    # 混合音频
    mixed = weights[0] * audio1 + weights[1] * audio2
    
    # 归一化
    max_val = np.max(np.abs(mixed))
    if max_val > 1.0:
        mixed = mixed / max_val
        
    return mixed 