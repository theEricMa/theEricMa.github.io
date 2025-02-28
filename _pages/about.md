---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I'm a third year Ph.D. Department of Computing (COMP) at Hong Kong Polytechnic University (PolyU). I am jointly advised by Prof. [Lei Zhang](https://www4.comp.polyu.edu.hk/~cslzhang/) at PolyU and Prof. [Zhen Lei](http://www.cbsr.ia.ac.cn/users/zlei/), [Xiangyu Zhu]() at Institute of Automation, Chinese Academy of Sciences (CASIA).

My research interest is 3D generation. 

<!-- I have published more than 100 papers at the top international AI conferences with total <a href='https://scholar.google.com/citations?user=F15mLDYAAAAJ&hl'>google scholar citations <strong><span id='total_cit'>260000+</span></strong></a> (You can also use google scholar badge <a href='https://scholar.google.com/citations?user=F15mLDYAAAAJ&hl'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>). -->


# 🔥 News
- *2025.02*: &nbsp;🎊 3 papers accepted by CVPR 2025, including 1 first-author paper.
- *2024.09*: &nbsp;🥳 1 paper accepted by NeurIPS 2024.
- *2024.07*: &nbsp;🎊 2 papers accepted by ECCV 2024, including 1 first-author paper.
- *2024.02*: &nbsp;🥳 1 paper accepted by CVPR 2024.
- *2023.02*: &nbsp;🎊 1 first-author paper accepted by CVPR 2023.

# 📝 Publications 

<!-- CVPR 2025 -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2025</div><img src='images/CVPR_2025.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

Progressive Rendering Distillation: Adapting Stable Diffusion for Instant Text-to-Mesh Generation without 3D Data
<!-- [](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf) -->

**Zhiyuan Ma**, Xinyue Liang, Rongyuan Wu, Xiangyu Zhu, Zhen Lei, Lei Zhang

 <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- First work to adapt Stable Diffusion as a text-to-mesh generator without 3D data.
- Achieved sub-second text-to-mesh generation in 4 steps.
- Introduced only 2.6% more parameters to the original Stable Diffusion model.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV 2024</div><img src='images/ECCV_2024.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[ScaleDreamer: Scalable Text-to-3D Synthesis with Asynchronous Score Distillation](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01046.pdf)

**Zhiyuan Ma**, Yuxiang Wei, Yabin Zhang, Xiangyu Zhu, Zhen Lei, Lei Zhang

<strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- First work to propose a score distillation method to train text-to-3D generator across multiple text prompts.
- Validated on 100K+ prompts using hyper-network, CNN and Transformer architectures.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2023</div><img src='images/CVPR_2023.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[OTAvatar : One-shot Talking Face Avatar with Controllable Tri-plane Rendering](https://openaccess.thecvf.com/content/CVPR2023/papers/Ma_OTAvatar_One-Shot_Talking_Face_Avatar_With_Controllable_Tri-Plane_Rendering_CVPR_2023_paper.pdf)

**Zhiyuan Ma**, Xiangyu Zhu, Guojun Qi, Zhen Lei, Lei Zhang

<strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- First work to adapt pre-trained 3D Face GANs for one-shot talking face generation.
- Explicit 3D rendering can handle extreme head movements.
</div>
</div>



- ``Arxiv 2024``  [DiffSpeaker: Speech-Driven 3D Facial Animation with Diffusion Transformer](https://arxiv.org/pdf/2402.05712) \|
**Zhiyuan Ma**, Xiangyu Zhu, Guojun Qi, Chen Qian, Zhaoxiang Zhang, Zhen Lei \| [code](https://github.com/theEricMa/DiffSpeaker)

- ``CVPR 2025`` [MVBoost: Boost 3D Reconstruction with Multi-View Refinement](https://arxiv.org/pdf/2411.17772) \|
Xiangyu Liu\*, Xiaomei Zhang\*, **Zhiyuan Ma**, Xiangyu Zhu, Zhen Lei \| [code](https://github.com/Piggy-ch/MVBoost)

- ``CVPR 2025`` [Pixel-level and Semantic-level Adjustable Super-resolution: A Dual-LoRA Approach](https://arxiv.org/pdf/2412.03017) \|
Lingchen Sun, Rongyuan Wu, **Zhiyuan Ma**, Shuaizheng Liu, Qiaosi Yi, Lei Zhang \| [code](https://github.com/csslc/PiSA-SR)

- ``NeurIPS 2024`` [One-Step Effective Diffusion Network for Real-World Image Super-Resolution](https://arxiv.org/pdf/2406.08177) \|
Rongyuan Wu\*, Lingchen Sun\*, **Zhiyuan Ma\***, Lei Zhang \| [code](https://github.com/cswry/OSEDiff)


- ``CVPR 2024`` [Dual memory networks: A versatile adaptation approach for vision-language models](https://openaccess.thecvf.com/content/CVPR2024/papers/Zhang_Dual_Memory_Networks_A_Versatile_Adaptation_Approach_for_Vision-Language_Models_CVPR_2024_paper.pdf) \| Yabin Zhang, Wenjie Zhu, Hui Tang, **Zhiyuan Ma**, Kaiyang Zhou, Lei Zhang \| [code](https://github.com/YBZh/DMN)

- ``ECCV 2024`` [Dense Multimodal Alignment for Open-Vocabulary 3D Scene Understanding](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06612.pdf) \| Ruihuang Li, Zhengqiang Zhang, Chenhang He, **Zhiyuan Ma**, Vishal M Patel, Lei Zhang \| [code](https://github.com/lslrh/DMA)



<!-- # 🎖 Honors and Awards
- *2021.10* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.09* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->

# 📖 Educations
- *2022.02 - now*, Ph.D. in Computer Science, Hong Kong Polytechnic University, Hong Kong, China.
- *2020.09 - 2022.01*, Master of Science in Electronic Engineering, Columbia University, New York, USA.
- *2016.09 - 2020.06*, Bachelor of Science in Information Engineering, Xi'an Jiaotong University, Xi'an, China.

<!-- # 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/) -->

# 💻 Internships
- *2022.01 - 2022.05*, CBSR, CASIA, Beijing, China.
- *2021.09 - 2022.01*, AI Research Lab, JD, Beijing, China.