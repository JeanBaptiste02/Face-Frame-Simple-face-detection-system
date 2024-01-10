from ProcessManager.FacialAnalysisProcessor import FacialAnalysisProcessor
from WebcamManager import WebcamManager
import time

vs = WebcamManager(0).start() #to start the webcam

FacialAnalysisProcessor()