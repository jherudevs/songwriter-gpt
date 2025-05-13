from scipy.io import wavfile
import numpy as np
import os

def ensure_mono(audio):
    if audio.ndim == 2:
        return audio.mean(axis=1)
    return audio

def normalize(audio):
    peak = np.max(np.abs(audio))
    return audio / peak if peak > 0 else audio

def overlay_audio(vibe_path, drum_path):
    print(f"[mix] Mixing {vibe_path} + {drum_path}")

    sr_vibe, vibe_data = wavfile.read(vibe_path)
    sr_drum, drum_data = wavfile.read(drum_path)

    if sr_vibe != sr_drum:
        raise ValueError("Sample rates do not match")

    # Convert to float and mono
    vibe_data = ensure_mono(vibe_data.astype(np.float32))
    drum_data = ensure_mono(drum_data.astype(np.float32))

    # Normalize and trim
    vibe_data = normalize(vibe_data)
    drum_data = normalize(drum_data)

    min_len = min(len(vibe_data), len(drum_data))
    vibe_data = vibe_data[:min_len]
    drum_data = drum_data[:min_len]

    mixed = 0.7 * vibe_data + 0.3 * drum_data
    mixed = mixed / np.max(np.abs(mixed)) if np.max(np.abs(mixed)) > 0 else mixed

    # Convert to int16 for export
    return (mixed * 32767).astype(np.int16), sr_vibe

