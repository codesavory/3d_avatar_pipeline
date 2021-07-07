# 3d_avatar_pipeline
Realistic 3D Avatar Pipeline using PIFuHD - Pixel Aligned Implicit Functions and RigNet - Neural Rigging Network

## Dependency and Setup
This project was tested in Windows 10 x64 System with Python 3.7 | Torch v1.8.0 TorchVision v0.9.0 on CPU with 16Gb of RAM using Anaconda Python Environment

### Linux User
```
conda create -n 3D_Avatar_Pipeline python=3.7
conda activate 3D_Avatar_Pipeline
```

### Install Necessary Libraries
```
pip install -r requirements.txt
```

#### For Windows user
The code has been tested on Windows 10 with cuda 10.1. The most important difference from Linux setup is, you need to download Windows-compiled Rtree from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#rtree), and install it by
`pip install Rtree‑0.9.4‑cp37‑cp37m‑win_amd64.whl` (64-bit system) or
`pip install Rtree‑0.9.4‑cp37‑cp37m‑win32.whl` (32-bit system). Other libraries can be installed in the same way as Linux setup instructions.

## Getting the checkpoints
Download the checkpoints into the base folder from [GDrive Link](https://drive.google.com/drive/folders/1mxUAOSpCZHdxcGYUGs9oJRvXkJOXzMEq?usp=sharing)

## Usage
The given script takes input photo(from ./input folder) and stores all the results(to ./Results/<image name>). Example usage -
```
python 3D_Avatar_Pipeline.py .\input\test.png
```
