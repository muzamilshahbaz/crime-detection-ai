from abc import ABC, abstractmethod


class Plugin(ABC):

    @abstractmethod
    def process(self, frame, detections):
        """
        Returns a list of Events
        """
        pass