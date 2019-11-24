#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

import os
import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
import IPython.display as ipd

audio_fpath = "../audio/"
audio_clips = os.listdir(audio_fpath)
final="../validation_audio"

for i in range(750):
    x, sr = librosa.load(audio_fpath+audio_clips[i],sr=None)
    print(type(x), type(sr))
    print(x.shape, sr)
    plt.figure(figsize=(12, 5))
    plt.axis('off')
    plt.xticks([])
    plt.yticks([])
    librosa.display.waveplot(x, sr=sr)
    X = librosa.stft(x)
    Xdb = librosa.amplitude_to_db(abs(X))
    plt.figure(figsize=(12, 5))
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
    plt.savefig(os.path.join(final,(audio_clips[i])+'.png'))
    plt.close()
