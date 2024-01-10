import cv2
import dlib

#Web cam manager
class WebcamManager:
    def __init__(self, src=0):
        self.video_capture = cv2.VideoCapture(src)
        self.detector = dlib.get_frontal_face_detector()
        self.faces = []

    def start(self):
        return self

    def read_frame(self):
        _, frame = self.video_capture.read()
        self.faces = self.detect_faces(frame)
        return frame

    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.detector(gray)
        return faces

    def stop(self):
        self.video_capture.release()
