from pathlib import Path

# 项目根目录
ROOT_DIR = Path(__file__).parent.parent.parent.parent

# 输出目录
OUTPUT_DIR = ROOT_DIR / "output"

# 模型配置
MODEL_CONFIGS = {
    "diffsinger": {
        "root": ROOT_DIR / "models" / "diffsinger",
        "configs": ROOT_DIR / "models" / "diffsinger" / "configs",
        "scripts": ROOT_DIR / "models" / "diffsinger" / "scripts",
        "path": ROOT_DIR / "models" / "diffsinger" / "saved_models"
    }
} 