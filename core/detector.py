from ultralytics import YOLO

from core.detection import Detection


class Detector:

    def __init__(self, model_path, confidence):

        print("[INFO] Loading model...")

        self.model = YOLO(model_path)

        self.confidence = confidence

        print("[INFO] AI Ready")

    def detect(self, frame):

        results = self.model.track(
            frame,
            persist=True,
            verbose=False
        )

        result = results[0]

        detections = []

        for box in result.boxes:

            tracker_id = None

            if box.id is not None:
                tracker_id = int(box.id)
                
            conf = float(box.conf[0])

            if conf < self.confidence:
                continue

            cls = int(box.cls[0])

            label = self.model.names[cls]

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            detections.append(

                Detection(
                    label=label,
                    confidence=conf,
                    x1=x1,
                    y1=y1,
                    x2=x2,
                    y2=y2,
                    tracker_id=tracker_id
                )

            )

        return detections