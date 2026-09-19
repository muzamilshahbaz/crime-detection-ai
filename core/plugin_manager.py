class PluginManager:

    def __init__(self):
        self.plugins = []

    def register(self, plugin):
        self.plugins.append(plugin)
        print(f"[PLUGIN] Loaded: {plugin.__class__.__name__}")

    def process(self, frame, detections):

        events = []

        for plugin in self.plugins:

            plugin_events = plugin.process(frame, detections)

            if plugin_events:
                events.extend(plugin_events)

        return events