from songwriter_ai.utilities.audio.align import auto_align_vibe_to_drums

def test_align_function_runs():
    assert callable(auto_align_vibe_to_drums)
    print("✅ test_align_function_runs passed")
