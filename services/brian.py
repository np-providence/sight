import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
brian_url = os.getenv("BRIAN_URL")
print(brian_url)

def identify(face_encodings, location):
    headers = {
                'content-type': 'application/json',
                'method': 'POST'
            }
    payload = {
            'faces': [face_encoding.tolist() for face_encoding in face_encodings],
            'location_id': location['id']
            }
    r = requests.post(brian_url + "/api/identify", data=json.dumps(payload), headers=headers)
    faces = json.loads(r.text)['faces']
    print(faces)
    return faces

def get_locations():
    headers = {
                'content-type': 'application/json',
                'method': 'GET'
            }
    r = requests.get(brian_url + "/api/location/all", headers=headers)
    locations = json.loads(r.text)
    return locations 


