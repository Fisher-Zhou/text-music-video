import os
import sys

# 设置PYTHONPATH，确保包导入正常
ROOT = os.path.dirname(os.path.abspath(__file__))
os.environ['PYTHONPATH'] = ROOT
sys.path.insert(0, ROOT)

if __name__ == "__main__":
    # 默认用acoustic.yaml配置
    config = os.path.join(ROOT, "configs", "acoustic.yaml")
    # 你也可以通过命令行参数传递config
    os.system(f'{sys.executable} "{os.path.join(ROOT, "scripts", "train.py")}" --config "{config}"') 