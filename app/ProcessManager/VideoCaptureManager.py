import cv2
import threading

#GUI Manager
class VideoCaptureManager:
    def __init__(self, webcam_manager, window_name="Face Frame"):
        self.webcam_manager = webcam_manager
        self.stopped = False
        self.window_name = window_name

    def initiate_video_streaming(self):
        threading.Thread(target=self.video_stream_update_loop, args=()).start()

    def video_stream_update_loop(self):
        while not self.stopped:
            frame = self.webcam_manager.read_frame()
            self.show_frame(frame)

            if cv2.waitKey(1) & 0xFF == ord("q") | ord("w"):
                self.stopped = True

        self.terminate_video_stream()

    def show_frame(self, frame):
        cv2.imshow(self.window_name, frame)

    def terminate_video_stream(self):
        cv2.destroyAllWindows()
        self.webcam_manager.stop()
