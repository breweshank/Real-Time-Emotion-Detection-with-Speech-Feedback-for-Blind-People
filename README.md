# Real-Time-Emotion-Detection-with-Speech-Feedback-for-Blind-People

This project utilizes **DeepFace**, **OpenCV**, and **pyttsx3** to analyze facial expressions in real-time from a webcam feed. The detected emotions are displayed on the screen and spoken out loud using text-to-speech (TTS).

## Features

✅ **Real-time emotion detection** using DeepFace  
✅ **Text-to-speech (TTS) feedback** using `pyttsx3`  
✅ **Multi-threading for smooth performance**  
✅ **Displays detected emotion on screen**  
✅ **Speaks the emotion only when it changes**  
✅ **Press 'q' to exit**  

## Installation

### Prerequisites
Ensure you have Python installed (Python 3.7+ recommended). Then, install the required dependencies using:

```sh
pip install opencv-python deepface pyttsx3 numpy
```

> **Note:** `pyttsx3` requires `espeak` (Linux) or `sapi5` (Windows) for text-to-speech functionality.

## Usage

Run the script:

```sh
python emotion_detection.py
```

The system will:
1. Open a webcam window.
2. Analyze emotions in real-time.
3. Display the detected emotion on the video feed.
4. Speak the emotion when it changes.

Press **'q'** to quit the program.

## Code Explanation

### 1️⃣ Emotion Detection with DeepFace
- The script captures frames from the webcam.
- `DeepFace.analyze()` detects emotions from the face.
- The **dominant emotion** is extracted and displayed on the screen.

### 2️⃣ Text-to-Speech (TTS) with pyttsx3
- When the detected emotion changes, the program **speaks the emotion** using `pyttsx3`.
- A **threaded speech function** ensures smooth processing without lagging the video feed.

### 3️⃣ Optimizations for Performance
- **Multi-threading** prevents lag in speech output.
- **Emotion change detection** avoids repetitive speech.
- **Time delay (2s)** between speeches prevents rapid voice output.

## Example Output

When the camera detects an emotion, the program will display and speak:

🖥️ **On Screen:**  
```
Happy
```

🔊 **Audio Output:**  
```
"You look Happy"
```

## Future Improvements
🚀 Add support for **multi-face detection**  
🎭 Expand to detect **age, gender, and race**  
📡 Integrate with **IoT for smart assistants**  

## GitHub Repository Setup

1️⃣ Create a `README.md` (this file)  
2️⃣ Add **`requirements.txt`**  

```sh
opencv-python  
deepface  
pyttsx3  
numpy  
```

3️⃣ Push to GitHub  

```sh
git init  
git add .  
git commit -m "Added real-time emotion detection with speech feedback"  
git push -u origin main  
```

## Contributions & Support
💡 Feel free to **fork, improve, and contribute**!  
🐛 Found a bug? Open an **issue**.  
⭐ If you like this, give it a **star** on GitHub!  

---

🎤 **Now your AI can see and speak emotions in real-time! and make blind people to see the beautifull emotion** 🚀

