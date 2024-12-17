import numpy as np
import scipy.io.wavfile as wav
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

def butter_lowpass_filter(data, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return lfilter(b, a, data)

# Load the audio file
file_path = "input_audio.wav"  #your file path
fs, audio_data = wav.read(file_path)

# Ensure mono audio and normalize
if len(audio_data.shape) > 1:  # Stereo to Mono
    audio_data = audio_data[:, 0]
audio_data = audio_data / np.max(np.abs(audio_data))

# Apply the low-pass filter
cutoff_freq = 3000  # Set cutoff frequency (in Hz)
filtered_audio = butter_lowpass_filter(audio_data, cutoff=cutoff_freq, fs=fs, order=6)

# Clamp the filtered audio to valid range
filtered_audio = np.clip(filtered_audio, -1.0, 1.0)

# Save the filtered audio
output_path = "output_audio.wav"
wav.write(output_path, fs, (filtered_audio * 32767).astype(np.int16))

# Plot original and filtered signals
time = np.linspace(0, len(audio_data) / fs, num=len(audio_data))
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(time, audio_data, label="Original")
plt.title("Original Audio Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, filtered_audio, label="Filtered", color="orange")
plt.title("Filtered Audio Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

plt.tight_layout()
plt.show()