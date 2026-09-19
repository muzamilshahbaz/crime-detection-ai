class Pipeline:

    def __init__(
        self,
        detector,
        visualizer,
        plugin_manager,
        event_manager
    ):
        self.detector = detector
        self.visualizer = visualizer
        self.plugin_manager = plugin_manager
        self.event_manager = event_manager

    def process(self, frame):

        detections = self.detector.detect(frame)

        events = self.plugin_manager.process(
            frame,
            detections
        )

        approved_events = self.event_manager.process(events)

        output = self.visualizer.draw(
            frame,
            detections
        )

        return output, approved_events