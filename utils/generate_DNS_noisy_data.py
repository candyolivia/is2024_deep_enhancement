# Select random interferer from train scenes

import shutil, random
import soundfile
from pydub import AudioSegment
import scipy.io.wavfile as wav
import os, random
import numpy as np

dirpath = '/DNS-Challenge-master/datasets_fullband/datasets_fullband/noise_fullband'
destDirectory = '/is2024_deep_enhancement/dataset/DNS3/noisy/set2/eval'
sourceDirectory = '/is2024_deep_enhancement/dataset/DNS3/noisy/set2/clean'

# import os
# for root, dirs, files in os.walk(dirpath):
#     for file in files:
#         if file.endswith("interferer_CH1.wav"):
#             interferer_filenames.append(random.choice(os.listdir(dirpath)))

audio_filenames = []

import os
for root, dirs, files in os.walk(sourceDirectory):
    for file in files:
        if file.endswith(".wav"):
            audio_filenames.append(os.path.join(root, file))


for idx, fname in enumerate(audio_filenames):
    srcpath = os.path.join(dirpath, fname)
    filename = fname.split('/')[-1][:-4] + '_mix_CH1.wav'
    destPath = os.path.join(destDirectory, filename)
    # print(destPath)
 
    source_wav = AudioSegment.from_wav(srcpath)
    source_wav = source_wav.set_frame_rate(44100)
    source_wav_path = (sourceDirectory + '/' + fname.split('/')[-1])

    # source_wav.export(source_wav_path, format = "wav")
    (source_rate, source_sig) = wav.read(source_wav_path)

    # print(len(source_sig))

    SNR_target = random.uniform(-5, 15)


    while True:
        try:
            random_interferer = (os.path.join(dirpath, random.choice(os.listdir(dirpath))))
            interferer_wav = AudioSegment.from_wav(random_interferer)
            break
        except:
            random_interferer = (os.path.join(dirpath, random.choice(os.listdir(dirpath))))
            pass

    
    interferer_wav = interferer_wav.set_channels(1)

    # if source_wav is longer than interferer_wav, repeat interferer_wav twice
    if (len(source_wav) > len(interferer_wav)):
        interferer_wav = interferer_wav * 4
    
    print(filename, SNR_target, random_interferer, sep=';')

    speech_dB = source_wav.dBFS
    noise_dB = interferer_wav.dBFS

    gain = (speech_dB - noise_dB) - SNR_target

    noise_SNRed = interferer_wav.apply_gain(gain)
    
    mixture_wav = noise_SNRed.overlay(source_wav)
    mixture_wav.export(destPath, format="wav")
    (mixture_rate, mixture_sig) = wav.read(destPath)
    mixture_sig = mixture_sig[:len(source_sig)]

    wav.write(destPath, mixture_rate, mixture_sig)

