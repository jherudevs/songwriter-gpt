import librosa
import soundfile as sf
import os
from scipy.io import wavfile

def time_stretch_to_bpm(filepath, original_bpm, target_bpm, target_sample_rate=None):
    print(f"[align] Time-stretching {filepath} from {original_bpm} → {target_bpm} BPM")

    # Load the vibe loop at native sample rate
    y, sr = librosa.load(filepath, sr=None)
    rate = target_bpm / original_bpm
    y_stretched = librosa.effects.time_stretch(y, rate=rate)

    # If drum sample rate is provided, resample to match
    if target_sample_rate and sr != target_sample_rate:
        print(f"[align] Resampling from {sr} Hz → {target_sample_rate} Hz")
        y_stretched = librosa.resample(y_stretched, orig_sr=sr, target_sr=target_sample_rate)
        sr = target_sample_rate

    # Save stretched version
    os.makedirs("outputs/stretched", exist_ok=True)
    base = os.path.basename(filepath).replace(".wav", "_stretched.wav")
    stretched_path = os.path.join("outputs/stretched", base)
    sf.write(stretched_path, y_stretched, sr)

    return stretched_path
