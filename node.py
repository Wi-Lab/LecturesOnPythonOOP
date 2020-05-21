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


class Node(NSPyObject):

    def __init__(self, scheduler, address):
        super().__init__()
        self._address = address
        self.scheduler = scheduler

    '''
        input args:
        packet: the packet that we want to transfer 
        node: destination node 
        at: the time at which we want this transfer happen
    '''

    def send(self, packet, node, at):
        class TransmitHandler(Handler):
            def __init__(self, node, packet):
                self.node = node
                self.packet = packet

            def execute(self):
                # deliver packet to destination node when event time arrived
                self.node.receive(self.packet)
        self.scheduler.schedule(Event(TransmitHandler(node, packet), at))

    '''
        input args:
        packet: the packet that we have received
    '''

    def receive(self, packet):
        print("Node <{}> received Packet with payload <{}> at <{}>".format(self._address, packet, self.scheduler._now))
