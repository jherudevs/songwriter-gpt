import librosa

def detect_bpm(filepath):
    print(f"[bpm_detector] Estimating BPM for: {filepath}")

    y, sr = librosa.load(filepath, sr=None)
    tempo = librosa.beat.tempo(y=y, sr=sr)[0]

    print(f"[bpm_detector] Estimated BPM: {tempo:.2f}")
    return tempo
