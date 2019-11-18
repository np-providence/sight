from capture.opencv import capture as opencv_capture 
from capture.picamera import capture as picamera_capture 
from dotenv import load_dotenv
import face_recognition
import cv2
import os

load_dotenv(verbose=True)

IS_PI = os.getenv("IS_PI") == "True"

capture_runtime = picamera_capture() if IS_PI else opencv_capture()

if __name__ == "__main__":
    process_frame = True
    face_locations = []

    while True:
        frame = next(capture_runtime)

        if process_frame:
            # Find faces
            face_locations = face_recognition.face_locations(frame)
            # Get their encodings
            face_encodings = face_recognition.face_encodings(frame, face_locations)

        process_frame = not process_frame

        # Invert to BGR before drawing
        frame = frame[:, :, ::-1]
        # Draw face boxes 
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 1)
        # Draw image 
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Be kind 
cv2.destroyAllWindows()

