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

node1 = Node('192.168.1.1')
node2 = Node('192.168.1.2')
node3 = Node('192.168.1.3')

try:
    node1.send(pf().create(pt.UDP), node2)
    node2.send(pf().create(pt.RTR), node1)
except Exception as e:
    print(e)


Simulator().run()
