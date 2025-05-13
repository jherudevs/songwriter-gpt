import os
import random
import time

random.seed(time.time())

def get_all_wav_files(directory):
    wavs = []
    for root, _, files in os.walk(directory):
        for f in files:
            if f.lower().endswith(".wav"):
                wavs.append(os.path.join(root, f))
    return wavs

def select_loops(vibe_name=None, drum_name=None):
    base_vibe_folder = "loops/vibe"
    drum_folder = "loops/drums"

    # 🎯 Vibe loop selection
    if vibe_name:
        vibe_folder = os.path.join(base_vibe_folder, vibe_name)
        vibe_loops = get_all_wav_files(vibe_folder)
    else:
        vibe_loops = get_all_wav_files(base_vibe_folder)

    if not vibe_loops:
        raise FileNotFoundError(f"No .wav files found for vibe: {vibe_name or 'ALL'}")

    # 🥁 Drum loop selection
    drum_loops = get_all_wav_files(drum_folder)
    if not drum_loops:
        raise FileNotFoundError("No .wav files found in loops/drums")

    vibe_path = random.choice(vibe_loops)
    drum_path = random.choice(drum_loops)

    print(f"[loop_selector] Selected: {vibe_path}, {drum_path}")
    return vibe_path, drum_path
