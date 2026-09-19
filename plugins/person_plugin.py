from core.plugin import Plugin
from core.event import Event


class PersonPlugin(Plugin):

    def process(self, frame, detections):

        events = []

        for detection in detections:

            if detection.label == "person":

                events.append(

                    Event(
                        name="PersonDetected",
                        confidence=detection.confidence,
                        description="Person detected"
                    )

                )

        return events