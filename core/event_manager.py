import time


class EventManager:

    def __init__(self, cooldown=5):

        self.cooldown = cooldown

        self.last_events = {}

    def process(self, events):

        approved = []

        current = time.time()

        for event in events:

            key = event.name

            if key not in self.last_events:

                self.last_events[key] = current

                approved.append(event)

                continue

            elapsed = current - self.last_events[key]

            if elapsed >= self.cooldown:

                self.last_events[key] = current

                approved.append(event)

        return approved