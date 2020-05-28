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

node1 = Node('192.168.1.1')
node2 = Node('192.168.1.2')
node3 = Node('192.168.1.3')

node1.send(pf().create("UDP"), node2)
node2.send(pf().create("RTR"), node1)


Simulator().run()
