import cv2
import dlib

#Camera
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
        self.identify_face_green_square(frame)
        return frame

    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.detector(gray)
        return faces

    def identify_face_green_square(self, frame):
        for face in self.faces:
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3) 
            
    def stop(self):
        self.video_capture.release()
