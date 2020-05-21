'''
    A Simple Event Driven Simulator
'''
from scheduler import Scheduler
from event import Event
from handler import Handler
from node import Node
from simulator import Simulator


node1 = Node('192.168.1.1')
node2 = Node('192.168.1.2')
node3 = Node('192.168.1.3')

node1.send("message from node1 to node 2", node2, 1.1)
node2.send("ack for message from node1", node1, 1.2)

node3.send("message from node3 to node1", node1, 0.4)

Simulator().run()
