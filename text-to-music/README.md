# OrpheusMelody 音乐生成系统

这是一个基于深度学习的音乐生成系统，可以自动生成完整的音乐作品，包括歌词、旋律、人声和伴奏。

## 功能特点

- 基于通义千问API生成原创歌词
- 根据歌词生成MIDI格式的旋律
- 合成自然的人声演唱
- 生成与风格匹配的伴奏
- 自动混音生成最终作品

## 安装要求

- Python 3.8+
- CUDA支持的GPU（推荐）
- 至少16GB内存
- 通义千问API密钥

## 安装步骤

1. 克隆仓库：
```bash
git clone https://github.com/yourusername/OrpheusMelody.git
cd OrpheusMelody
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 配置API密钥：
```bash
# 在lyrics_generator.py中设置你的通义千问API密钥
# 或者通过环境变量设置：
export DASHSCOPE_API_KEY=your_api_key
```

4. 下载预训练模型：
```bash
# 需要下载以下模型：
# - MIDI-LM（用于旋律生成）
# - Vocal-LM（用于人声合成）
# - LDM（用于伴奏生成）
```

## 使用方法

1. 基本使用：
```python
from main import MusicGenerator

generator = MusicGenerator()
theme = "夏天的欢乐时光"
style = "流行"
output_path = generator.generate_music(theme, style)
```

2. 高级使用：
```python
from lyrics_generator import LyricsGenerator
from melody_generator import MelodyGenerator
from vocal_synthesizer import VocalSynthesizer
from accompaniment_generator import AccompanimentGenerator
from audio_mixer import AudioMixer

# 自定义每个步骤
lyrics_gen = LyricsGenerator(api_key="your_api_key")
lyrics = lyrics_gen.generate("爱情", "流行")

melody_gen = MelodyGenerator()
melody_gen.generate(lyrics, "流行", "melody.mid")

vocal_synth = VocalSynthesizer()
vocal_synth.synthesize(lyrics, "melody.mid", "vocal.wav")

accomp_gen = AccompanimentGenerator()
accomp_gen.generate("vocal.wav", "流行", "accompaniment.wav")

mixer = AudioMixer()
mixer.mix("vocal.wav", "accompaniment.wav", "final_song.wav")
```

## 注意事项

1. 首次运行需要下载预训练模型，可能需要较长时间
2. 建议使用GPU运行以获得更好的性能
3. 生成的人声质量取决于模型训练数据
4. 可以通过调整参数来优化生成效果
5. 通义千问API有调用频率限制，请合理使用

## 项目结构

```
OrpheusMelody/
├── main.py                 # 主程序入口
├── lyrics_generator.py     # 歌词生成模块（使用通义千问API）
├── melody_generator.py     # 旋律生成模块
├── vocal_synthesizer.py    # 人声合成模块
├── accompaniment_generator.py  # 伴奏生成模块
├── audio_mixer.py          # 混音模块
├── requirements.txt        # 依赖列表
└── README.md              # 项目说明
```

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request来改进项目。 