# Title: Are Recent Deep Learning-Based Speech Enhancement Methods Ready to Confront Real-World Noisy Environments?

## Under construction

## Abstract:

Recent advancements in speech enhancement techniques have ignited interest in improving speech quality and intelligibility. However, the effectiveness of recently proposed methods is unclear. In this paper, a comprehensive analysis of modern deep learning-based speech enhancement approaches is presented. Through evaluations using the Deep Suppression Noise and Clarity Enhancement Challenge datasets, we assess the performances of three methods: Denoiser, DeepFilterNet3, and FullSubNet+. Our findings reveal nuanced performance differences among these methods, with varying efficacy across datasets. While objective metrics offer valuable insights, they struggle to represent complex scenarios with multiple noise sources. Leveraging ASR-based methods for these scenarios shows promise but may induce critical hallucination effects. Our study emphasizes the need for ongoing research to refine techniques for diverse real-world environments.

## Authors:

Candy Olivia Mawalim, Shogo Okada, and Masashi Unoki
(Japan Advanced Institute of Science and Technology)

## Paper Link:

Link to our INTERSPEECH paper is available here (TBD).

## Audio samples:
Audio samples are available on our demo page (TBD).

## Code Description:

This repository contains the code used in the paper `Are Recent Deep Learning-Based Speech Enhancement Methods Ready to Confront Real-World Noisy Environments?` accepted to Interspeech 2024.

The project is organized as follows:

```
[dataset]: Required data for running the experiments
    |-- CEC2
        |-- train
            |-- clean
            |-- noisy
        |-- eval
            |-- set1
                |-- clean
                |-- noisy
            |-- set2
                |-- clean
                |-- noisy
    |-- DNS3
        |-- eval
            |-- set1
                |-- clean
                |-- noisy
            |-- set2
                |-- clean
                |-- noisy

[demo_sounds]: Sound files for demonstrations

[models]: Speech enhancement models utilized in the experiments
    |-- DeepFilterNet
    |-- denoiser
    |-- FullSubNet-plus

[utils]: Code for preprocessing, extracting Whisper transcript, and calculating WER & Beep-PER

... (and so on)
```

## Installation:

- Clone this repository:
```
git clone https://github.com/your_username/your_repo_name.git
```

- Install the dependencies:
```
pip install -r requirements.txt
```

- Running the Code:

To run the code, follow these steps:

  - Download the necessary data (the 2nd Clarity Enhancement challenge (CEC2) and the 3rd Deep Noise Supressor (DNS) challenge datasets). The links to the data could be found on the `References`.
  - Locate the downloaded dataset to the `dataset` directory.
  - Run the relevant script(s) according to the speech enhancement model in `models` directory. Instructions on which scripts to run can be found in the corresponding folders. More information on each model also could be found at the link of the original source available on the `References`.

- Example usage of fine-tuning denoiser (after navigate to `denoiser` subsubfolder):

```
./train.py continue_pretrained=dns64 demucs.hidden=64 dset=train restart=1
```

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
