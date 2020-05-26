'''
    A Simple Event Driven Simulator
'''
from scheduler import Scheduler
from event import Event
from handler import Handler
from node import Node
from simulator import Simulator
from packet import Packet


node1 = Node('192.168.1.1')
node2 = Node('192.168.1.2')
node3 = Node('192.168.1.3')

node1.send(Packet().type('TCP').size(1*2**10), node2)
node2.send(Packet().type("UDP").size(2**20), node1)


Simulator().run()
