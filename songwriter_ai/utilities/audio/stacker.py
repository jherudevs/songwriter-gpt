#!/usr/bin/env python3

from songwriter_ai.utilities.audio.align import time_stretch_to_bpm
from songwriter_ai.utilities.audio.mix import overlay_audio
from songwriter_ai.utilities.audio.extend_loop_to_bars import extend_loop_to_bars
from songwriter_ai.utilities.metadata.bpm_detector import detect_bpm
from songwriter_ai.utilities.file_ops.loop_selector import select_loops
from scipy.io import wavfile
import os
from pathlib import Path

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
    base_output = Path("outputs/stacks") / f"stacked_{Path(vibe_path).stem}_{Path(drum_path).stem}.wav"
    os.makedirs(base_output.parent, exist_ok=True)

    # Mix and get audio object (but don't export yet)
    mixed_audio, sample_rate  = overlay_audio(stretched_vibe_path, drum_path)

    # Extend and export final file
    extended_output = extend_loop_to_bars(
        mixed_audio,
        sample_rate,
        bar_count=90,
        output_name=f"stacked_{Path(vibe_path).stem}_{Path(drum_path).stem}",
        bpm=drum_bpm  # <-- pass it in directly
    )


    return extended_output

if __name__ == "__main__":
    run_stacker()
