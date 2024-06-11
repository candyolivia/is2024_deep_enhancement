# Copy data from source directory to the project and preprocessing

import glob, os, shutil
from pydub import AudioSegment

source_dir = "/CEC_repository/CEC2/clarity_CEC2_core.v1_1/clarity_CEC2_data/clarity_data/dev/scenes/"
dest_dir = "/is2024_deep_enhancement/dataset/CEC2/eval/set1/clean/"

files = glob.iglob(os.path.join(source_dir, "*_target_CH1.wav"))
for file in files:
    if os.path.isfile(file):
        sound = AudioSegment.from_wav(file)
        sound = sound.set_channels(1)
        sound.export(dest_dir + file.split('/')[-1], format="wav")
