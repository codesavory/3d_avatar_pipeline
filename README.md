# Realistic 3D Avatar Pipeline in Realtime
Realistic 3D Avatar Pipeline using PIFuHD - Pixel Aligned Implicit Functions and RigNet - Neural Rigging Network

## Dependency and Setup
This project was tested in Windows 10 x64 System with Python 3.7 | Torch v1.8.0 TorchVision v0.9.0 on CPU with 16Gb of RAM using Anaconda Python Environment.

### Constraints
open3D supports only Python v3.6, 3.7 and 3.8

```
conda create -n 3D_Avatar_Pipeline python=3.7
conda activate 3D_Avatar_Pipeline
```

### Clone the GitHub Repository and the Submodules
```
git clone https://github.com/codesavory/3d_avatar_pipeline
git submodule init
git submodule update
```


### Install Necessary Libraries
```
pip install torch==1.8.0 torchvision==0.9.0
pip install -r requirements.txt
```

## If using CUDA 10.1 (TO TEST)
```
conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=10.2 -c pytorch
```

### Install some torch depencies
```
pip install torch-scatter -f https://pytorch-geometric.com/whl/torch-1.8.0+cu101.html
pip install torch-sparse -f https://pytorch-geometric.com/whl/torch-1.8.0+cu101.html
pip install torch-cluster -f https://pytorch-geometric.com/whl/torch-1.8.0+cu101.html
pip install torch-spline-conv -f https://pytorch-geometric.com/whl/torch-1.8.0+cu101.html
pip install torch-geometric
```

#### For Windows user
Download Windows-compiled Rtree from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#rtree), and install it by
`pip install Rtree‑0.9.4‑cp37‑cp37m‑win_amd64.whl` (64-bit system) or
`pip install Rtree‑0.9.4‑cp37‑cp37m‑win32.whl` (32-bit system). Other libraries can be installed in the same way as Linux setup instructions.

## Getting the checkpoints
Download the checkpoints into the base folder from [GDrive Link](https://drive.google.com/drive/folders/1mxUAOSpCZHdxcGYUGs9oJRvXkJOXzMEq?usp=sharing) extract and rename it as Checkpoints

## Usage
The given script takes input photo(from ./input folder) and stores all the results(to ./Results/<image name>). Example usage -
```
python 3D_Avatar_Pipeline.py .\input\test.png
```
