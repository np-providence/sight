import picamera

# Pi Runtime 
def capture():
    with picamera.PiCamera() as camera:
        camera.framerate = 24
        time.sleep(2) # Warm up
        while True:
            image = []
            camera.capture(image, 'bgr')
            yield image
