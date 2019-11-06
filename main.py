from uuid import getnode as get_mac
from picamera import PiCamera 
from time import sleep
from io import BytesIO

if __name__ == "__main__":
    # Create an in-memory stream
    my_stream = BytesIO()
    camera = PiCamera()
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture(my_stream, 'jpeg')
