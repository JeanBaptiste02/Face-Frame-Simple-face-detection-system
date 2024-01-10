import cv2
import dlib
import numpy as np  # Ajoutez cette ligne pour importer NumPy

# Camera
class WebcamManager:
    def __init__(self, src=0):
        self.video_capture = cv2.VideoCapture(src)
        self.detector = dlib.get_frontal_face_detector()
        self.age_net = cv2.dnn.readNetFromCaffe('deploy_age.prototxt', 'age_net.caffemodel')
        self.faces = []

    def start(self):
        return self

    def read_frame(self):
        _, frame = self.video_capture.read()
        self.faces = self.detect_faces(frame)
        self.identify_face_green_square(frame)
        self.predict_and_display_age(frame)
        return frame

    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.detector(gray)
        return faces

    def identify_face_green_square(self, frame):
        for face in self.faces:
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    def predict_and_display_age(self, frame):
        for face in self.faces:
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            face_roi = frame[y:y + h, x:x + w]
            blob = cv2.dnn.blobFromImage(face_roi, scalefactor=1.0, size=(227, 227),
                                        mean=(78.4263377603, 87.7689143744, 114.895847746), swapRB=False)
            self.age_net.setInput(blob)
            age_preds = self.age_net.forward()
            age = int(np.argmax(age_preds[0]) / 10)
            print(f"Age: {age}")


    def stop(self):
        self.video_capture.release()
