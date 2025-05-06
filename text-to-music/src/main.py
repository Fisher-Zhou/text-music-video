import os
from pathlib import Path
from dotenv import load_dotenv
from tqdm import tqdm

from text_to_music.core import MusicGenerator
from text_to_music.utils.logger import setup_logger
from text_to_music.config import OUTPUT_DIR

def main():
    # 加载环境变量
    load_dotenv()
    
    # 设置日志
    logger = setup_logger("music_generator")
    
    try:
        # 创建音乐生成器
        generator = MusicGenerator()
        
        # 设置参数
        theme = "夏天的欢乐时光"
        style = "流行"
        output_dir = OUTPUT_DIR / "generated_music"
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # 生成音乐
        logger.info(f"开始生成音乐，主题：{theme}，风格：{style}")
        final_path = generator.generate_music(theme, style, str(output_dir))
        
        logger.info(f"音乐生成完成！最终文件保存在: {final_path}")
        
    except Exception as e:
        logger.error(f"生成过程中出现错误: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    main() 