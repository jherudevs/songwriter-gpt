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

def overlay_audio(vibe_path, drum_path, output_path):
    print(f"[mix] Mixing {vibe_path} + {drum_path} → {output_path}")

    sr_vibe, vibe_data = wavfile.read(vibe_path)
    sr_drum, drum_data = wavfile.read(drum_path)

    print(f"[mix] Sample rates — Vibe: {sr_vibe}, Drum: {sr_drum}")
    if sr_vibe != sr_drum:
        raise ValueError("Sample rates do not match")

    # Convert to float and mono
    vibe_data = ensure_mono(vibe_data.astype(np.float32))
    drum_data = ensure_mono(drum_data.astype(np.float32))

    # Normalize each before mixing
    vibe_data = normalize(vibe_data)
    drum_data = normalize(drum_data)

    # Trim to match
    min_len = min(len(vibe_data), len(drum_data))
    vibe_data = vibe_data[:min_len]
    drum_data = drum_data[:min_len]

    # Mix with boosted vibe
    mixed = 0.7 * vibe_data + 0.3 * drum_data

    # Final normalization
    max_amp = np.max(np.abs(mixed))
    print(f"[mix] Final mix peak: {max_amp}")
    if max_amp > 0:
        mixed = mixed / max_amp

    # Scale and convert back to int16
    mixed = (mixed * 32767).astype(np.int16)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    wavfile.write(output_path, sr_vibe, mixed)
