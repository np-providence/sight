from capture.opencv import capture as opencv_capture 

opencv_capture_runtime = opencv_capture()

if __name__ == "__main__":
    process_frame = True
    while True:
        if process_frame:
            print(next(opencv_capture_runtime))
        process_frame = not process_frame
