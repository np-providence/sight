from capture.picamera import capture as picamera_capture 
from services.brian import identify
import face_recognition
import os


capture_runtime = picamera_capture()

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
            print(face_encodings)

        process_frame = not process_frame


