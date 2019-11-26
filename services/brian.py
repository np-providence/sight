import os
from dotenv import load_dotenv
import requests

load_dotenv()
brian_url = os.getenv("BRIAN_URL")
print(brian_url)

def identify(face_encodings):
    r = requests.post(brian_url + "/identify", data = {
                "face": [face_encoding for face_encoding in face_encodings]
            }
        )
    print(r.text)

