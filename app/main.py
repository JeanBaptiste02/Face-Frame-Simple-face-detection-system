from ProcessManager.FacialAnalysisProcessor import FacialAnalysisProcessor
from ProcessManager.VideoCaptureManager import VideoCaptureManager
from app.Webcam.WebcamManager import WebcamManager
import time


filters = ['glasses.png', 'sunglasses.png', 'sunglasses1.png', 'sunglasses2.png', \
        'dog.png', 'rabbit.png','moustache.png', 'moustache1.png', 'ironman.png', 'capAmerica.png']

vs = WebcamManager(0).start() #to start the webcam

FacialAnalysisProcessor()

fc = FacialAnalysisProcessor(filters)
gui = VideoCaptureManager(vs,fc,'output')