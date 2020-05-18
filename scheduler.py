

class Scheduler:

    def __init__(self):
        self._events = []
        self._now = 0.0

    def run(self):
        while len(self._events) > 0:
            ev = self._events.pop(0)
            self._now = ev._time
            ev.run()

    def schedule(self, event):
        self._events.append(event)
        self._events.sort(key=lambda x: x._time, reverse=False)

    def listEvents(self):
        for event in self._events:
            print(event, " at ", event._time)
