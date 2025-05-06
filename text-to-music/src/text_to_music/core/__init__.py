from .lyrics_generator import LyricsGenerator
from .melody_generator import MelodyGenerator
from .vocal_synthesizer import VocalSynthesizer
from .accompaniment_generator import AccompanimentGenerator
from .audio_mixer import AudioMixer

class MusicGenerator:
    def __init__(self):
        self.lyrics_generator = LyricsGenerator()
        self.melody_generator = MelodyGenerator()
        self.vocal_synthesizer = VocalSynthesizer()
        self.accompaniment_generator = AccompanimentGenerator()
        self.audio_mixer = AudioMixer()

    def generate_music(self, theme: str, style: str, output_dir: str) -> str:
        """生成完整的音乐
        
        Args:
            theme: 主题
            style: 风格
            output_dir: 输出目录
            
        Returns:
            str: 最终音频文件路径
        """
        # 生成歌词
        lyrics = self.lyrics_generator.generate(theme, style)
        
        # 生成旋律
        midi_path = f"{output_dir}/melody.mid"
        self.melody_generator.generate(lyrics, style, midi_path)
        
        # 合成人声
        vocal_path = f"{output_dir}/vocal.wav"
        self.vocal_synthesizer.synthesize(lyrics, midi_path, vocal_path)
        
        # 生成伴奏
        acc_path = f"{output_dir}/accompaniment.wav"
        self.accompaniment_generator.generate(vocal_path, style, acc_path)
        
        # 混音
        final_path = f"{output_dir}/final_mix.wav"
        self.audio_mixer.mix(vocal_path, acc_path, final_path)
        
        return final_path 