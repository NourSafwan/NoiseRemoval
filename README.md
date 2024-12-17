# Audio Noise Reduction using DSP

This project implements an audio noise reduction tool using **Digital Signal Processing (DSP)** techniques, specifically a **Low-Pass Butterworth Filter**. The app filters out high-frequency noise from an input audio file, producing a cleaner output audio.

---

## 📌 Features
- Reduces high-frequency noise using a **Butterworth Low-Pass Filter**.
- Supports **.wav** audio files.
- Saves the filtered audio to a new file.
- Provides waveform visualizations for both the original and filtered audio.

---

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites
Make sure you have the following installed:
- Python 3.7 or higher
- Required libraries: `numpy`, `scipy`, `matplotlib`

Install the dependencies using:
```bash
pip install numpy scipy matplotlib
```

---

### 🔧 Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/NourSafwan/NoiseRemoval.git
   cd NoiseRemoval
   ```

2. **Prepare Your Audio File**:
   - Place your input audio file (`input_audio.wav`) in the project directory.
   - Ensure it is in **.wav format**.

3. **Run the Script**:
   Execute the following command:
   ```bash
   python noise_reduction.py
   ```

4. **Output**:
   - The cleaned audio file will be saved as `output_audio.wav` in the same directory.
   - Two plots will be displayed, showing the original and filtered audio waveforms.

---

## 🛠 How It Works

### Techniques Used:
1. **Low-Pass Butterworth Filter**:
   - Allows frequencies below a specified cutoff to pass and attenuates higher frequencies.
   - Ideal for removing high-frequency noise like static and hiss.

2. **Signal Normalization**:
   - Ensures audio is scaled within a fixed range for consistency.

3. **Waveform Visualization**:
   - Plots the original and filtered audio for comparison.

### Parameters:
- **Cutoff Frequency**: Default is set to **3000 Hz** (suitable for speech).
- **Filter Order**: Determines the sharpness of the filter.

---

## 📂 Project Structure
```
NoiseRemoval/
│
├── noise_reduction.py    # Main Python script
├── input_audio.wav       # Input noisy audio file
├── output_audio.wav      # Output filtered audio file
└── README.md             # Project documentation
```

---

## 📊 Visual Output
- **Original Audio**: The waveform of the input noisy audio.
- **Filtered Audio**: The waveform of the denoised audio after applying the low-pass filter.

---

## 🧪 Example Usage

Here’s an example of the Python script:

```python
import numpy as np
import scipy.io.wavfile as wav
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

def butter_lowpass_filter(data, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return lfilter(b, a, data)

# Load input audio
fs, audio_data = wav.read("input_audio.wav")
audio_data = audio_data / np.max(np.abs(audio_data))  # Normalize

# Apply low-pass filter
filtered_audio = butter_lowpass_filter(audio_data, cutoff=3000, fs=fs, order=6)

# Save output
wav.write("output_audio.wav", fs, (filtered_audio * 32767).astype(np.int16))
```

---

## 🧩 Limitations
- The current implementation works best for **high-frequency noise**.
- It may not fully remove **broadband or dynamic noise**.
- For advanced noise reduction (e.g., environmental noise), consider using **Spectral Subtraction** or AI-based methods.

---

## 📝 Future Improvements
- Implement **Spectral Subtraction** for better noise removal.
- Add support for other audio formats like MP3.
- Incorporate machine learning for adaptive noise suppression.

---

## 💡 Resources
- [Butterworth Filter](https://en.wikipedia.org/wiki/Butterworth_filter)
- [SciPy Signal Documentation](https://docs.scipy.org/doc/scipy/reference/signal.html)
- [Audio Processing with Python](https://librosa.org/)

---

## 🤝 Contributing
Contributions are welcome! If you'd like to improve this project, fork the repository and create a pull request.

1. Fork the project
2. Create a new branch: `git checkout -b feature-branch`
3. Commit your changes: `git commit -m "Add feature"`
4. Push to the branch: `git push origin feature-branch`
5. Open a Pull Request

---

## 🧑‍💻 Author
**NourSafwan**  
[GitHub](https://github.com/NourSafwan) | [LinkedIn](https://www.linkedin.com/in/noursafwan)
