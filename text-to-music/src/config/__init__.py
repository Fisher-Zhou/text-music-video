from pathlib import Path
import os
import yaml

# 基础路径
BASE_DIR = Path(__file__).parent.parent.parent
SRC_DIR = BASE_DIR / "src"
MODELS_DIR = BASE_DIR / "models"
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
TEMP_DIR = BASE_DIR / "temp"
LOG_DIR = BASE_DIR / "logs"

# 确保目录存在
for dir_path in [MODELS_DIR, DATA_DIR, OUTPUT_DIR, TEMP_DIR, LOG_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)

# 加载配置文件
def load_config(config_path):
    """加载YAML配置文件"""
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

# 模型配置
MODEL_CONFIGS = {
    "melody_lm": {
        "path": MODELS_DIR / "melody_lm",
        "checkpoint": MODELS_DIR / "melody_lm" / "checkpoint.pt",
        "config": MODELS_DIR / "melody_lm" / "config.json"
    },
    "musicgen": {
        "path": MODELS_DIR / "musicgen",
        "checkpoint": MODELS_DIR / "musicgen" / "musicgen_small.pt",
        "config": MODELS_DIR / "musicgen" / "config.json"
    },
    "diffsinger": {
        "path": MODELS_DIR / "diffsinger",
        "checkpoint": MODELS_DIR / "diffsinger" / "opencpop" / "model.pt",
        "config": MODELS_DIR / "diffsinger" / "opencpop" / "config.yaml",
        "root": MODELS_DIR / "diffsinger" / "DiffSinger-2.5.0",
        "scripts": MODELS_DIR / "diffsinger" / "DiffSinger-2.5.0" / "scripts",
        "configs": MODELS_DIR / "diffsinger" / "DiffSinger-2.5.0" / "configs"
    }
}

# 设备配置
DEVICE = "cuda" if os.environ.get("CUDA_VISIBLE_DEVICES") else "cpu"

# API配置
QWEN_API_KEY = os.getenv("QWEN_API_KEY", "")

# 日志配置
LOG_LEVEL = "INFO" 