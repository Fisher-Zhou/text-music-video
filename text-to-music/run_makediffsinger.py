import subprocess

config = 'ljspeech_mds.yaml'
subprocess.run(['makediffsinger', 'preprocess', config], check=True)
print('MakeDiffSinger 数据准备完成！') 