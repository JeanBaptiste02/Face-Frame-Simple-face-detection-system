from ProcessManager.WebcamManager import WebcamManager
from ProcessManager.VideoCaptureManager import VideoCaptureManager
import time

if __name__ == "__main__":
    cam = WebcamManager(0).start()  # Start the webcam

    vcm = VideoCaptureManager(cam, 'Face Frame')

    vcm.initiate_video_streaming()

    time.sleep(60)  # will run for 60 sec

    vcm.stopped = True  # stop the video stream
