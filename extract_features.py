import librosa
import numpy as np

INPUT_FILE = "barking_sound.wav"
print('hello1')
# Load the recorded audio
y, sr = librosa.load(INPUT_FILE, sr=None)

# Extract duration
duration = librosa.get_duration(y=y, sr=sr)

# Extract frequency (mean fundamental frequency)
spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
frequency = np.mean(spectral_centroid) if spectral_centroid.size > 0 else 0

print(f"Extracted Features - Duration: {duration:.2f} sec, Frequency: {frequency:.2f} Hz")
