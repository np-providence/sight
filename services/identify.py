import os
import requests

base_url = os.getenv("API_URL")

def identify(face_encodings):
    r = requests.post(base_url + "/identify", data = {"face": [face_encoding for face_encoding in face_encodings]})
    print(r.text)

