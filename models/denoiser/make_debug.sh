#!/bin/bash
# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
# authors: adiyoss and adefossez

path=egs/train/tr
if [[ ! -e $path ]]; then
    mkdir -p $path
fi
# python3 -m denoiser.audio dataset/train/noisy > $path/noisy.json
# python3 -m denoiser.audio dataset/train/clean > $path/clean.json


python3 -m denoiser.audio /media/candy/SSD/CEC2/scenes/data_augmentation/vctk_mix > $path/noisy_vctk_dev.json
python3 -m denoiser.audio /media/candy/SSD/CEC2/scenes/data_augmentation/vctk_dev_44kHz > $path/clean_vctk_dev.json

# python3 -m denoiser.audio /media/candy/SSD/CEC2/scenes/dev_mono_44kHz > $path/noisy.json
# python3 -m denoiser.audio /media/candy/SSD/CEC2/scenes/target_mono_44kHz > $path/clean.json


python3 -m denoiser.audio /media/candy/SSD/CEC2/scenes/train_mono_44kHz/noisy > $path/noisy.json
python3 -m denoiser.audio /media/candy/SSD/CEC2/scenes/train_mono_44kHz/clean > $path/clean.json

python3 -m denoiser.audio /media/candy/SSD/CEC2/scenes/train_mono_left_44kHz/noisy > $path/noisy_left.json
python3 -m denoiser.audio /media/candy/SSD/CEC2/scenes/train_mono_left_44kHz/clean > $path/clean_left.json

python3 -m denoiser.audio /media/candy/SSD/CEC2/scenes/train_mono_right_44kHz/noisy > $path/noisy_right.json
python3 -m denoiser.audio /media/candy/SSD/CEC2/scenes/train_mono_right_44kHz/clean > $path/clean_right.json