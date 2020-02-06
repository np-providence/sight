from capture.opencv import capture as opencv_capture 
from services.brian import identify, get_locations
import face_recognition
import cv2
import os

capture_runtime = opencv_capture()

if __name__ == "__main__":
    locations = get_locations()

    print('Locations:')
    index = 0
    for location in locations:
        print('[{}] - {}'.format(index, location['name']))
        index += 1

    selected_location_index = int(input('Select location of camera: '))

    location = locations[selected_location_index]

    process_frame = True
    face_locations = []
    face_names = []

    while True:
        frame = next(capture_runtime)

        if process_frame:
            # Find faces
            face_locations = face_recognition.face_locations(frame)
            # Get their encodings
            face_encodings = face_recognition.face_encodings(frame, face_locations)
            if len(face_encodings) > 0:
                face_names = identify(face_encodings, location)

        process_frame = not process_frame

        # Invert to BGR before drawing
        frame = frame[:, :, ::-1]
        # Draw face boxes 
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 1)
            cv2.rectangle(frame, (left, bottom + 10), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left, bottom + 7), font, 0.3, (255, 255, 255), 1)
        # Draw image 
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Be kind 
cv2.destroyAllWindows()

