'''
    A Simple Event Driven Simulator
'''
from scheduler import Scheduler
from event import Event
from handler import Handler
from node import Node
from simulator import Simulator
from packet import Packet
from packetFactory import PacketFactory as pf
from packet import PacketType as pt
from wirelessPhy import WirelessPhy
from mac import Mac
from application import Application
from queue import Queue

node1 = Node().Phy(WirelessPhy()).Mac(Mac()).Queue(Queue(10)).App(Application(5))

node1._app.start(1.0)
node1._app.stop(10.0)

Simulator().run()
