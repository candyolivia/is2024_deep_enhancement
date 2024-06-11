# Title: Are Recent Deep Learning-Based Speech Enhancement Methods Ready to Confront Real-World Noisy Environments?

## Under construction

## Abstract:

Recent advancements in speech enhancement techniques have ignited interest in improving speech quality and intelligibility. However, the effectiveness of recently proposed methods is unclear. In this paper, a comprehensive analysis of modern deep learning-based speech enhancement approaches is presented. Through evaluations using the Deep Suppression Noise and Clarity Enhancement Challenge datasets, we assess the performances of three methods: Denoiser, DeepFilterNet3, and FullSubNet+. Our findings reveal nuanced performance differences among these methods, with varying efficacy across datasets. While objective metrics offer valuable insights, they struggle to represent complex scenarios with multiple noise sources. Leveraging ASR-based methods for these scenarios shows promise but may induce critical hallucination effects. Our study emphasizes the need for ongoing research to refine techniques for diverse real-world environments.

## Authors:

Candy Olivia Mawalim, Shogo Okada, and Masashi Unoki
(Japan Advanced Institute of Science and Technology)

## Paper Link:

[Link to your paper on the INTERSPEECH website] (https://www.isca-speech.org/)

## Audio samples:
Audio samples are available on our [demo page] (https://www.isca-speech.org/).

## Code Description:

This repository contains the code used in the paper `Are Recent Deep Learning-Based Speech Enhancement Methods Ready to Confront Real-World Noisy Environments?` accepted to Interspeech 2024.

The code is organized as follows:

```
[folder 1]: Description of the contents (e.g., data preprocessing scripts)
[folder 2]: Description of the contents (e.g., model implementation)
[folder 3]: Description of the contents (e.g., evaluation scripts)
... (and so on)
```

Dependencies:

This code requires the following dependencies:
```
Python [version]
[dependency 1] ([Optional: installation instructions])
[dependency 2] ([Optional: installation instructions])
... (and so on)
```

## Installation:

Clone this repository:
Bash
git clone https://github.com/your_username/your_repo_name.git
Use code with caution.
content_copy
Install the dependencies:
Bash
pip install -r requirements.txt
Use code with caution.
content_copy
Running the Code:

To run the code, follow these steps:

Download the necessary data (if applicable). Instructions on how to obtain the data can be found in the [folder name] directory.
Navigate to the root directory of the project:
```
Bash
cd your_repo_name
```
Use code with caution.
content_copy
Run the relevant script(s). Instructions on which scripts to run can be found in the corresponding folders.
Example Usage:

Bash
python train.py --config config.json
Use code with caution.
content_copy

## Citation:

If you use this code in your research, please cite the following paper:
```
@inproceedings{mawalim_interspeech24,
  author    = {Candy Olivia Mawalim and Shogo Okada and Masashi Unoki},
  title     = {[Are Recent Deep Learning-Based Speech Enhancement Methods Ready to Confront Real-World Noisy Environments?]},
  booktitle = {{Proc. INTERSPEECH 2024}},
  year      = {2024},
  pages		= {TBD},
  doi 		= {TBD}
}
```

**License:**

This code is licensed under the MIT license. See the LICENSE file for details.

## References:
We referred to the following repositories and resources in our code:
- https://github.com/microsoft/DNS-Challenge for dataset of the Deep Noise Suppressor challenge
- https://claritychallenge.org/docs/cec2/data/cec2_data for dataset of the 2nd Clarity Enhancement challenge 
- https://www.openslr.org/14/ for Beep dictionary
- https://github.com/facebookresearch/denoiser for implementation and pre-trained weights for Denoiser model
- https://github.com/Rikorose/DeepFilterNet for implementation and pre-trained weights for DeepFilterNet model
- https://github.com/RookieJunChen/FullSubNet-plus for implementation and pre-trained weights for FullSubNet+ model
