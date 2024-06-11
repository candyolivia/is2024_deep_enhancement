#!/usr/bin/env bash

/usr/bin/python3 speech_enhance/tools/calculate_metrics.py \
  -R /media/candy/SSD/CEC2/scenes/dev_mono_44kHz/clean \
  -E /media/candy/SSD/CEC2/scenes/dev_mono_44kHz/enhanced_deepFilter \
  -M SI_SDR,STOI,WB_PESQ,NB_PESQ \
  -S DNS_1 \
  -D /media/candy/SSD/CEC2/scenes/dev_mono_44kHz
