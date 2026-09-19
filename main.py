import cv2

from camera import Camera
from config import *

from core.detector import Detector
from core.visualizer import Visualizer
from core.plugin_manager import PluginManager
from core.event_manager import EventManager
from core.pipeline import Pipeline

from plugins.person_plugin import PersonPlugin

camera = Camera(CAMERA_SOURCE)
camera.connect()

detector = Detector(MODEL_PATH, CONFIDENCE)

visualizer = Visualizer()

plugin_manager = PluginManager()
plugin_manager.register(PersonPlugin())

event_manager = EventManager()

pipeline = Pipeline(
    detector,
    visualizer,
    plugin_manager,
    event_manager
)

while True:

    success, frame = camera.read()

    if not success:
        break

    output, events = pipeline.process(frame)

    for event in events:
        print(event)

    cv2.imshow(WINDOW_NAME, output)

    if cv2.waitKey(1) == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()