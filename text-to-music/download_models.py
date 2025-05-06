import os
import subprocess
import requests
import zipfile
import tarfile
from tqdm import tqdm
from pathlib import Path

class ModelDownloader:
    def __init__(self):
        self.base_dir = Path("models")
        self.models = {
            "musicgen": {
                "url": "https://huggingface.co/facebook/musicgen-small/resolve/main/pytorch_model.bin",
                "path": self.base_dir / "musicgen" / "pytorch_model.bin"
            },
            "diffsinger": {
                "url": "https://github.com/openvpi/DiffSinger/releases/download/pretrain/opencpop.zip",
                "path": self.base_dir / "diffsinger" / "opencpop.zip"
            },
            "riffusion": {
                "url": "https://huggingface.co/riffusion/riffusion-model-v1/resolve/main/pytorch_model.bin",
                "path": self.base_dir / "riffusion" / "pytorch_model.bin"
            }
        }
        
    def download_file(self, url, path):
        """下载文件并显示进度条"""
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        
        with open(path, 'wb') as f, tqdm(
            desc=path.name,
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for data in response.iter_content(chunk_size=1024):
                size = f.write(data)
                bar.update(size)
                
    def extract_zip(self, zip_path, extract_path):
        """解压zip文件"""
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
            
    def clone_git_repo(self, repo_url, target_dir):
        """克隆git仓库"""
        subprocess.run(["git", "clone", repo_url, target_dir], check=True)
        
    def download_models(self):
        """下载所有模型"""
        # 确保基础目录存在
        self.base_dir.mkdir(parents=True, exist_ok=True)
        
        # 下载可以直接获取的模型
        for model_name, model_info in self.models.items():
            print(f"\n正在下载 {model_name}...")
            model_path = model_info["path"]
            model_path.parent.mkdir(parents=True, exist_ok=True)
            
            if not model_path.exists():
                self.download_file(model_info["url"], model_path)
                
                # 如果是zip文件，解压
                if model_path.suffix == '.zip':
                    print(f"正在解压 {model_name}...")
                    self.extract_zip(model_path, model_path.parent)
                    
        # 克隆git仓库
        print("\n正在克隆git仓库...")
        repos = {
            "DiffSinger": "https://github.com/openvpi/DiffSinger.git",
            "NNSVS": "https://github.com/nnsvs/nnsvs.git",
            "So-VITS-SVC": "https://github.com/svc-develop-team/so-vits-svc.git"
        }
        
        for repo_name, repo_url in repos.items():
            target_dir = self.base_dir / repo_name.lower().replace("-", "_")
            if not target_dir.exists():
                print(f"正在克隆 {repo_name}...")
                self.clone_git_repo(repo_url, target_dir)
                
    def setup_environment(self):
        """设置环境"""
        print("\n正在设置环境...")
        # 创建requirements.txt文件
        requirements = """
torch>=2.0.0
torchaudio>=2.0.0
numpy>=1.21.0
librosa>=0.9.0
soundfile>=0.10.3
pydub>=0.25.1
requests>=2.26.0
tqdm>=4.62.0
scipy>=1.7.0
dashscope>=1.10.0
transformers>=4.30.0
huggingface_hub>=0.16.0
"""
        
        with open("requirements.txt", "w") as f:
            f.write(requirements)
            
        print("请运行以下命令安装依赖：")
        print("pip install -r requirements.txt")
        
if __name__ == "__main__":
    downloader = ModelDownloader()
    downloader.download_models()
    downloader.setup_environment()
    print("\n所有模型下载完成！") 