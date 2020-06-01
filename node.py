'''
    This file models a simple network node

    node will have some functionalities as below:
        methods:
            send -> called when we want to transmit a data packet
            receive -> called when a data packet received




        attributes:
            _address -> this attr models nodes address(each node must have a unique address)
'''
from NSPyObject import NSPyObject
from handler import Handler
from event import Event
from simulator import Simulator
from packet import Packet
from wirelessPhy import WirelessPhy
from mac import Mac
from application import Application
from queue import Queue


class PhyNotDefinedYetException(Exception):

    def __init__(self):
        self.message = f"Physical not defined for node yet"
        super().__init__(self.message)


class MacNotDefinedYetException(Exception):

    def __init__(self):
        self.message = f"Mac Layer not defined for node yet"
        super().__init__(self.message)


class QueueNotDefinedYetException(Exception):

    def __init__(self):
        self.message = f"Queue Layer not defined for node yet"
        super().__init__(self.message)


class Node(NSPyObject):

    def __init__(self):
        super().__init__()

    def Phy(self, phy: WirelessPhy):
        self._phy = phy
        return self

    def Mac(self, mac: Mac):
        if self._phy is None:
            raise PhyNotDefinedYetException()
        self._mac = mac
        self._mac.down(self._phy)
        self._phy.up(self._mac)
        return self

    def Queue(self, queue: Queue):
        if self._mac is None:
            raise MacNotDefinedYetException()
        self._queue = queue
        self._queue.down(self._mac)
        return self

    def App(self, app: Application):
        if self._queue is None:
            raise MacNotDefinedYetException()
        if self._mac is None:
            raise MacNotDefinedYetException()
        self._app = app
        self._app.down(self._queue)
        self._mac.up(self._app)
        return self
