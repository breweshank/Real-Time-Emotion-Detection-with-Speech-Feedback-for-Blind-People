import cv2
import pyttsx3
import threading
import time
from deepface import DeepFace

# Initialize Text-to-Speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speech speed

def speak_emotion(emotion):
    """Speak detected emotion in a separate thread."""
    def run():
        engine.say(f"You look {emotion}")
        engine.runAndWait()
    speech_thread = threading.Thread(target=run)
    speech_thread.daemon = True  # Ensures thread stops on exit
    speech_thread.start()

# Start video capture
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height

last_emotion = "Neutral"
last_speak_time = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    try:
        # Detect emotions
        result = DeepFace.analyze(frame, actions=["emotion"], enforce_detection=False)

        if result and "dominant_emotion" in result[0]:
            detected_emotion = result[0]["dominant_emotion"].capitalize()
        else:
            detected_emotion = "Neutral"

        # Display detected emotion
        cv2.putText(frame, detected_emotion, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Speak only if emotion changes and enough time has passed
        if detected_emotion != last_emotion and detected_emotion != "Neutral" and time.time() - last_speak_time > 2:
            speak_emotion(detected_emotion)
            last_speak_time = time.time()

        last_emotion = detected_emotion

    except Exception as e:
        print("Error:", e)

    cv2.imshow("Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
