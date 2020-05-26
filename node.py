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


class Node(NSPyObject):

    def __init__(self, address, txRate=float(2**20)):  # default rate set to 1Mbps
        super().__init__()
        self._address = address
        self._transmissionRate = txRate

    '''
        input args:
        packet: the packet that we want to transfer 
        node: destination node 
    '''

    def send(self, packet: Packet, node: 'Node'):
        class TransmitHandler(Handler):
            def __init__(self, node, packet: Packet):
                self.node = node
                self.packet = packet

            def execute(self):
                # deliver packet to destination node when event time arrived
                self.node.receive(self.packet)

        # calculate txTime based on txRate and packet size
        Simulator().after(packet._size/self._transmissionRate, TransmitHandler(node, packet))

    '''
        input args:
        packet: the packet that we have received
    '''

    def receive(self, packet: Packet):
        print("Node <{}> received Packet with size <{}> at <{}>".format(self._address, packet._size, Simulator().now()))
