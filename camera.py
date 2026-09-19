import cv2


class Camera:
    def __init__(self, source):
        self.source = source
        self.cap = None

    def connect(self):
        self.cap = cv2.VideoCapture(self.source)

        if not self.cap.isOpened():
            raise Exception(f"Cannot open camera: {self.source}")

        # Request an extreme resolution to force the device to its hardware limit
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        
        print(f"[INFO] Connected to: {self.source}")

    def read(self):
        if self.cap is None:
            return False, None

        return self.cap.read()

    def release(self):
        if self.cap:
            self.cap.release()

        print("[INFO] Camera released")