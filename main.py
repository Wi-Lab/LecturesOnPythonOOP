'''
    A Simple Event Driven Simulator
'''
from scheduler import Scheduler
from event import Event
from handler import Handler


class PrintHello(Handler):
    def execute(self):
        print("Hello from PrintHello Handler")


class PrintGoodBye(Handler):
    def execute(self):
        print("GoodBye from PrintGoodBye Handler")


MyScheduler = Scheduler()

MyScheduler.schedule(Event(PrintGoodBye(), 1.0))
MyScheduler.schedule(Event(PrintHello(), 0.1))

MyScheduler.run()
