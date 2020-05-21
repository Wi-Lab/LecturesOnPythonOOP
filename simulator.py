
from scheduler import Scheduler
from event import Event
from handler import Handler
from NSPyObject import NSPyObject


class Simulator(NSPyObject):
    '''
    Singleton pattern usage
    '''

    _instance = None
    _scheduler = None

    def __new__(cls):
        if cls._instance is None:  # this is the first time we create an object of this type
            cls._instance = super(Simulator, cls).__new__(cls)
            cls._scheduler = Scheduler()
        return cls._instance

    def at(self, time, handler):
        Simulator._scheduler.schedule(Event(handler, time))

    def now(self):
        return Simulator._scheduler._now

    def run(self):
        Simulator._scheduler.run()
