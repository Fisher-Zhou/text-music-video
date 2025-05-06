from setuptools import setup, find_packages

setup(
    name="text_to_music",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "tqdm",
        "python-dotenv",
        "numpy",
        "torch",
        "torchaudio",
        "librosa",
        "soundfile",
    ],
    python_requires=">=3.8",
) 