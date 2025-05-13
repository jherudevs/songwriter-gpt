from pydub import AudioSegment
import math
import numpy as np
import os
from pathlib import Path
from scipy.io.wavfile import write
from songwriter_ai.utilities.metadata.bpm_detector import detect_bpm

def extend_loop_to_bars(mixed_audio, sample_rate, bar_count, output_name, bpm):
    output_path = Path("outputs/stacks") / f"{output_name}_x{bar_count}bars.wav"

    # Estimate BPM
    # NOTE: You must use the original filepath for bpm detection
    # or pass bpm explicitly
    
    seconds_per_bar = (60 / bpm) * 4
    desired_samples = int(bar_count * seconds_per_bar * sample_rate)

    loop_count = math.ceil(desired_samples / len(mixed_audio))
    looped = np.tile(mixed_audio, loop_count)[:desired_samples]

    write(output_path, sample_rate, looped.astype(np.int16))
    print(f"✅ Exported extended beat: {output_path}")
    return output_path
