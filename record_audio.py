import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

# Configuration
SAMPLE_RATE = 44100  # 44.1 kHz sample rate (CD quality)
DURATION = 5  # Record for 5 seconds
OUTPUT_FILE = "barking_sound.wav"

print("Recording barking sound...")

# Capture audio from the microphone
audio_data = sd.rec(int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
sd.wait()  # Wait until recording is finished

# Save the recorded audio as a WAV file
wav.write(OUTPUT_FILE, SAMPLE_RATE, audio_data)
print(f"Audio saved as {OUTPUT_FILE}")
