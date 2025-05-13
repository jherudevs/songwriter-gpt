#!/usr/bin/env python3

from songwriter_ai.utilities.audio.align import time_stretch_to_bpm
from songwriter_ai.utilities.audio.mix import overlay_audio
from songwriter_ai.utilities.metadata.bpm_detector import detect_bpm
from songwriter_ai.utilities.file_ops.loop_selector import select_loops
from scipy.io import wavfile
import os

def run_stacker(vibe_name=None, drum_name=None, output_dir="outputs"):
    # Select loops (random or by name)
    vibe_path, drum_path = select_loops(vibe_name, drum_name)

    # Detect BPMs
    vibe_bpm = detect_bpm(vibe_path)
    drum_bpm = detect_bpm(drum_path)

    # Get drum sample rate before stretching
    drum_sr, _ = wavfile.read(drum_path)

    # Time-stretch vibe to match drum BPM
    stretched_vibe_path = time_stretch_to_bpm(vibe_path, vibe_bpm, drum_bpm, target_sample_rate=drum_sr)
    
    # Mix and export
    output_path = os.path.join("outputs/stacks", f"stacked_{os.path.basename(vibe_path)}_{os.path.basename(drum_path)}")
    os.makedirs("outputs/stacks", exist_ok=True)

    overlay_audio(stretched_vibe_path, drum_path, output_path)

    print(f"✅ Stacked loop saved at: {output_path}")

if __name__ == "__main__":
    run_stacker()
