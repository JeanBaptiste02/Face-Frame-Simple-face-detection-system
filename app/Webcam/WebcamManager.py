import cv2
import threading

class WebcamManager:
    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        self.frame = None
        self.stopped = False

    def start(self):
        # Start a new thread to read frames from the webcam
        threading.Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return

            _, self.frame = self.stream.read()

    def read(self):
        # Return the most recent frame
        return self.frame

    def stop(self):
        # Stop the thread
        self.stopped = True
        self.stream.release()