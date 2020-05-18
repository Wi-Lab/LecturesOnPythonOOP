'''
Modifying Attributes

We can change the value of attributes based on some behavior:
'''


class Node:
    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac
        self.queue = []

    # instance method
    def description(self):
        return "Node n1 with IP<{}> and MAC<{}>".format(self.ip, self.mac)

    # instance method
    def sendPacket(self, payload, dst):
        return "Sending {} to node {}".format(payload, dst.ip)

    # instance method that modifies attributes of instance
    def receivePacket(self, newPacket):
        self.queue.append(newPacket)

    def queueLength(self):
        return "Queue length is {}".format(len(self.queue))


'''
Here, we added a method to receive a packet, which updates the nodes queue.
'''

n1 = Node('192.168.1.2', 'C9:2A:4E:61:AD:C7')
n2 = Node('192.168.1.3', 'C9:2A:4E:61:AD:C8')

print(n1.queueLength())

n1.receivePacket("Packet 1")

print(n1.queueLength())

n1.receivePacket("Packet 2")
