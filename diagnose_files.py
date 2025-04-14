import librosa
import numpy as np
from pathlib import Path

def process_single_file(mp3_path):
    try:
        y, sr = librosa.load(mp3_path, sr=16000)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13, hop_length=160, n_fft=2048)
        np.save(f"processed_akan/{Path(mp3_path).stem}.npy", mfcc)
        print(f"✅ Processed {mp3_path}")
    except Exception as e:
        print(f"❌ Failed {mp3_path}: {str(e)}")

process_single_file("datasets/raw_data/wavs/ak_gh_image_0203_u129_1_1688634700791_16197")