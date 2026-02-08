<<<<<<< HEAD
# InstantSplat
An unofficial implementation of InstantSplat, an sparse-view, SfM-free framework for large-scale scene reconstruction method using Gaussian Splatting.
Uses [Rerun](https://rerun.io/) to visualize, [Gradio](https://www.gradio.app) for an interactive UI, and [Pixi](https://pixi.sh/latest/) for a easy installation

<p align="center">
    <a title="Website" href="https://instantsplat.github.io/" target="_blank" rel="noopener noreferrer" style="display: inline-block;">
        <img src="https://www.obukhov.ai/img/badges/badge-website.svg">
    </a>
    <a href='https://huggingface.co/spaces/pablovela5620/instant-splat'><img src='https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue'></a>
    <a title="arXiv" href="https://arxiv.org/abs/2403.20309" target="_blank" rel="noopener noreferrer" style="display: inline-block;">
        <img src="https://www.obukhov.ai/img/badges/badge-pdf.svg">
    </a>
    <a title="Github" href="https://github.com/pablovela5620/InstantSplat" target="_blank" rel="noopener noreferrer" style="display: inline-block;">
        <img src="https://img.shields.io/github/stars/pablovela5620/InstantSplat?label=GitHub%20%E2%98%85&logo=github&color=C8C" alt="badge-github-stars">
    </a>
    <a title="Social" href="https://x.com/pablovelagomez1" target="_blank" rel="noopener noreferrer" style="display: inline-block;">
        <img src="https://www.obukhov.ai/img/badges/badge-social.svg" alt="social">
    </a>
  </p>

<p align="center">
  <img src="media/final_instantsplat.gif" alt="example output" width="720" />
</p>

## Install and Run
### Using Pixi
Make sure you have the [Pixi](https://pixi.sh/latest/#installation) package manager installed
=======

<h2 align="center"> <a href="https://arxiv.org/abs/2403.20309">InstantSplat: Sparse-view <a href="https://arxiv.org/abs/2403.20309"> Gaussian Splatting in Seconds </a>

<h5 align="center">

[![arXiv](https://img.shields.io/badge/Arxiv-2403.20309-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2403.20309) [![Gradio](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/kairunwen/InstantSplat) 
[![Home Page](https://img.shields.io/badge/Project-Website-green.svg)](https://instantsplat.github.io/) [![X](https://img.shields.io/badge/-Twitter@Zhiwen%20Fan%20-black?logo=twitter&logoColor=1D9BF0)](https://x.com/WayneINR/status/1774625288434995219)  [![youtube](https://img.shields.io/badge/Demo_Video-E33122?logo=Youtube)](https://youtu.be/fxf_ypd7eD8) [![youtube](https://img.shields.io/badge/Tutorial_Video-E33122?logo=Youtube)](https://www.youtube.com/watch?v=JdfrG89iPOA&t=347s)
</h5>

<div align="center">
This repository is the official implementation of InstantSplat, a sparse-view framework for large-scale scene reconstruction method using Gaussian Splatting.
InstantSplat supports 3D-GS, 2D-GS, and Mip-Splatting.
</div>
<br>

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Free-view Rendering](#free-view-rendering)
- [TODO List](#todo-list)
- [Get Started](#get-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Acknowledgement](#acknowledgement)
- [Citation](#citation)


## Free-view Rendering
https://github.com/zhiwenfan/zhiwenfan.github.io/assets/34684115/748ae0de-8186-477a-bab3-3bed80362ad7

## TODO List
- [x] Support 2D-GS
- [ ] Long sequence cross window alignment
- [ ] Support Mip-Splatting

## Get Started

### Installation
1. Clone InstantSplat and download pre-trained model.
>>>>>>> upstream/main
```bash
git clone https://github.com/pablovela5620/InstantSplat.git
cd InstantSplat
<<<<<<< HEAD
pixi run app
```

All commands can be listed using `pixi task list`
### Using Docker
If you'd rather use docker, you can just run
```
git clone https://github.com/pablovela5620/InstantSplat.git
cd InstantSplat
docker-compose up
=======
mkdir -p mast3r/checkpoints/
wget https://download.europe.naverlabs.com/ComputerVision/MASt3R/MASt3R_ViTLarge_BaseDecoder_512_catmlpdpt_metric.pth -P mast3r/checkpoints/
```

2. Create the environment (or use pre-built docker), here we show an example using conda.
```bash
conda create -n instantsplat python=3.10.13 cmake=3.14.0 -y
conda activate instantsplat
conda install pytorch torchvision pytorch-cuda=12.1 -c pytorch -c nvidia  # use the correct version of cuda for your system
pip install -r requirements.txt
pip install submodules/simple-knn
pip install submodules/diff-gaussian-rasterization
pip install submodules/fused-ssim
```

1. Optional but highly suggested, compile the cuda kernels for RoPE (as in CroCo v2).
```bash
# DUST3R relies on RoPE positional embeddings for which you can compile some cuda kernels for faster runtime.
cd croco/models/curope/
python setup.py build_ext --inplace
```

Alternative: use the pre-built docker image: pytorch/pytorch:2.1.2-cuda11.8-cudnn8-devel
```
docker pull dockerzhiwen/instantsplat_public:2.0
```
if docker failed to produce reasonable results, try Installation step again within the docker.

### Usage
1. Data preparation (download our pre-processed data from: [Hugging Face](https://huggingface.co/datasets/kairunwen/InstantSplat) or [Google Drive](https://drive.google.com/file/d/1Z17tIgufz7-eZ-W0md_jUlxq89CD1e5s/view))
```bash
  cd <data_path>
  # then do whatever data preparation
```

1. Command
```bash
  # InstantSplat train and output video (no GT reference, render by interpolation) using the following command.
  # Users can place their data in the 'assets/examples/<scene_name>/images' folder and run the following command directly.
  bash scripts/run_infer.sh

  # InstantSplat train and evaluate (with GT reference) using the following command.
  bash scripts/run_eval.sh
>>>>>>> upstream/main
```

## Hosted Demo
Demos can be found on huggingface spaces, local version is recommended to avoid GPU timeouts!

<a href='https://huggingface.co/spaces/pablovela5620/instant-splat'><img src='https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue'></a>

## Acknowledgements
Thanks to the original InstantSplat, Gaussian Splatting, and Dust3r repos!

[InstantSplat](https://github.com/NVlabs/InstantSplat)
```bibtex
@misc{fan2024instantsplat,
        title={InstantSplat: Sparse-view Gaussian Splatting in Seconds},
        author={Zhiwen Fan and Kairun Wen and Wenyan Cong and Kevin Wang and Jian Zhang and Xinghao Ding and Danfei Xu and Boris Ivanovic and Marco Pavone and Georgios Pavlakos and Zhangyang Wang and Yue Wang},
        year={2024},
        eprint={2403.20309},
        archivePrefix={arXiv},
        primaryClass={cs.CV}
      }
```
[Gaussian Splatting](https://github.com/graphdeco-inria/gaussian-splatting)
```bibtex
@Article{kerbl3Dgaussians,
      author       = {Kerbl, Bernhard and Kopanas, Georgios and Leimk{\"u}hler, Thomas and Drettakis, George},
      title        = {3D Gaussian Splatting for Real-Time Radiance Field Rendering},
      journal      = {ACM Transactions on Graphics},
      number       = {4},
      volume       = {42},
      month        = {July},
      year         = {2023},
      url          = {https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/}
}
```
[Dust3r](https://github.com/naver/dust3r)
```bibtex
@inproceedings{dust3r_cvpr24,
      title={DUSt3R: Geometric 3D Vision Made Easy}, 
      author={Shuzhe Wang and Vincent Leroy and Yohann Cabon and Boris Chidlovskii and Jerome Revaud},
      booktitle = {CVPR},
      year = {2024}
}

@misc{dust3r_arxiv23,
      title={DUSt3R: Geometric 3D Vision Made Easy}, 
      author={Shuzhe Wang and Vincent Leroy and Yohann Cabon and Boris Chidlovskii and Jerome Revaud},
      year={2023},
      eprint={2312.14132},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
