import os
import traceback
from text_to_music.core.lyrics_generator import LyricsGenerator
from text_to_music.core.melody_generator import MelodyGenerator
from text_to_music.core.vocal_synthesizer import VocalSynthesizer
from text_to_music.core.accompaniment_generator import AccompanimentGenerator
from text_to_music.core.audio_mixer import AudioMixer

def self_check():
    output_dir = "self_check_output"
    os.makedirs(output_dir, exist_ok=True)
    results = []
    try:
        print("[1] 检查歌词生成模块...")
        lyrics_gen = LyricsGenerator()
        lyrics = lyrics_gen.generate("自检主题", "流行")
        assert isinstance(lyrics, str) and len(lyrics) > 0
        lyrics_path = os.path.join(output_dir, "lyrics.txt")
        with open(lyrics_path, "w", encoding="utf-8") as f:
            f.write(lyrics)
        results.append("歌词生成模块：正常")
    except Exception as e:
        results.append(f"歌词生成模块：异常 - {e}\n{traceback.format_exc()}")

    try:
        print("[2] 检查旋律生成模块...")
        melody_gen = MelodyGenerator()
        midi_path = os.path.join(output_dir, "melody.mid")
        melody_gen.generate(lyrics, "流行", midi_path)
        assert os.path.exists(midi_path)
        results.append("旋律生成模块：正常")
    except Exception as e:
        results.append(f"旋律生成模块：异常 - {e}\n{traceback.format_exc()}")

    try:
        print("[3] 检查人声合成模块...")
        vocal_syn = VocalSynthesizer()
        vocal_path = os.path.join(output_dir, "vocal.wav")
        vocal_syn.synthesize(lyrics, midi_path, vocal_path)
        assert os.path.exists(vocal_path)
        results.append("人声合成模块：正常")
    except Exception as e:
        results.append(f"人声合成模块：异常 - {e}\n{traceback.format_exc()}")

    try:
        print("[4] 检查伴奏生成模块...")
        acc_gen = AccompanimentGenerator()
        acc_path = os.path.join(output_dir, "accompaniment.wav")
        acc_gen.generate(vocal_path, "流行", acc_path)
        assert os.path.exists(acc_path)
        results.append("伴奏生成模块：正常")
    except Exception as e:
        results.append(f"伴奏生成模块：异常 - {e}\n{traceback.format_exc()}")

    try:
        print("[5] 检查混音模块...")
        mixer = AudioMixer()
        final_path = os.path.join(output_dir, "final_mix.wav")
        mixer.mix(vocal_path, acc_path, final_path)
        assert os.path.exists(final_path)
        results.append("混音模块：正常")
    except Exception as e:
        results.append(f"混音模块：异常 - {e}\n{traceback.format_exc()}")

    print("\n==== 自检结果 ====")
    for r in results:
        print(r)

if __name__ == "__main__":
    self_check() 