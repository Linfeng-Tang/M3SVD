# M3SVD: Multi-Modal Multi-Scene Video Dataset

<div align="center">
  <p>
    <a href="https://arxiv.org/abs/2503.23359">
      <img src="https://img.shields.io/badge/Paper-CVPR%202026-blue" alt="Paper">
    </a>
    <a href="https://github.com/Linfeng-Tang/VideoFusion">
      <img src="https://img.shields.io/badge/Code-VideoFusion-green" alt="Code">
    </a>
    <a href="https://pan.baidu.com/s/1FhUirShTQ02N5Dl3pgl-PA?pwd=M2VD">
      <img src="https://img.shields.io/badge/Baidu-Images-2319DC?logo=baidu&logoColor=white" alt="Baidu Images">
    </a>
    <a href="https://pan.baidu.com/s/1R6HOSMXCHSiPEywU0GK_hw?pwd=M2VD">
      <img src="https://img.shields.io/badge/Baidu-Videos-2319DC?logo=baidu&logoColor=white" alt="Baidu Videos">
    </a>
    <a href="https://pan.baidu.com/s/1R6HOSMXCHSiPEywU0GK_hw?pwd=M2VD">
      <img src="https://img.shields.io/badge/GoogleDrive-Videos-4285F4?logo=googledrive&logoColor=white" alt="GoogleDrive Videos">
    </a>
  </p>
</div>

---

## ✨ News  

- **[2026]** Our paper **“VideoFusion: A Spatio-Temporal Collaborative Network for Multi-modal Video Fusion and Restoration”** has been accepted to **CVPR 2026**.  [[Paper](https://arxiv.org/abs/2503.23359)] [[Code](https://github.com/Linfeng-Tang/VideoFusion)]

- **[2025]** [**M3SVD**](https://github.com/Linfeng-Tang/M3SVD) dataset is officially released.

---

# 📖 Introduction

**M3SVD (Multi-Modal Multi-Scene Video Dataset)** is a large-scale infrared-visible (IR-VI) video dataset designed for:

- 🔥 Multi-modal video fusion  
- 🌙 Low-light / degraded video restoration  
- 📹 Spatio-temporal modeling research  

---

# 🎥 Scenario Schematic

<p align="center">
  <img src="Video/Demo/datasets.png" width="92%">
</p>
<p align="center">
  <i>Visualization of representative scenarios in M3SVD. 
    The dataset contains 220 temporally synchronized infrared-visible (IR-VI) video pairs 
    with 153,797 aligned frames in total, captured at a resolution of 640×480 and 30 FPS.</i>
</p>

---

# 🏗 Data Processing Workflow
<p align="center">
  <img src="assets/Workflow.jpg" width="92%">
</p>

# Dataset Comparison (vs. prior works)
<p align="center">
  <img src="assets/Dataset_Comparison.jpg" width="92%">
</p>


---

# 🎞 Video Demo

Example sequences (GIF previews):

![Demo GIF](Video/Demo/0118_1803.gif)

![Demo GIF](Video/Demo/1230_1154.gif)

![Demo GIF](Video/Demo/0114_1551.gif)

![Demo GIF](Video/Demo/0115_1831.gif)

---

# 📦 Dataset Availability

- Current release: **Test split**
- Full dataset access: Please contact  
  **linfeng0419@gmail.com**

We are open to academic collaboration and research usage.

---

# 🔗 Related Work Using M3SVD

### [VideoFusion](https://arxiv.org/abs/2503.23359) (CVPR 2026)
Spatio-temporal collaborative network for multi-modal video fusion and restoration.  [[Paper](https://arxiv.org/abs/2503.23359)] [[Code](https://github.com/Linfeng-Tang/VideoFusion)]

---

# 📝 Citation

If you use M3SVD in your research, please cite:

```bibtex
@inproceedings{Tang2026VideoFusion,
  title     = {VideoFusion: A Spatio-Temporal Collaborative Network for Multi-modal Video Fusion and Restoration},
  author    = {Tang, Linfeng and Wang, Yeda and Gong, Meiqi and Li, Zizhuo and Deng, Yuxin and Yi, Xunpeng and Li, Chunyu and Zhang, Hao and Xu, Han and Ma, Jiayi},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year      = {2026}
}
