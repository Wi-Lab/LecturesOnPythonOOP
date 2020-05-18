
from handler import Handler


class Event:

    def __init__(self, handler, time):
        self._handler = handler
        self._time = time

    def run(self):
        self._handler.execute()
