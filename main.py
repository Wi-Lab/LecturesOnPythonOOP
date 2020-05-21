'''
Static Members
'''


class Node:
    # static member
    numberOfTotalNodes = 0

    def __init__(self, name, ip, mac):
        self.name = name  # Public
        self._ip = ip    # protected
        self._mac = mac  # private
        self.__queue = []  # private
        Node.numberOfTotalNodes += 1  # increament total node cunter when a new node created

    # instance method
    def description(self):
        return "Node <{}> with IP<{}> and MAC<{}>".format(self.name, self._ip, self._mac)

    # instance method
    def sendPacket(self, payload, dst):
        return "Sending {} to node {}".format(payload, dst._ip)

    # instance method that modifies attributes of instance
    def receivePacket(self, newPacket):
        self.queue.append(newPacket)

    def queueLength(self):
        return "Queue length is {}".format(len(self.__queue))

    @staticmethod
    def totalNodes():
        return "Total nodes count is: {} ".format(Node.numberOfTotalNodes)


print(Node.totalNodes())
node1 = Node('node1', "192.168.1.1", 'C9:2A:4E:61:AD:C8')
print(Node.totalNodes())
node2 = Node('node2', "192.168.1.2", 'C9:2A:4E:61:BD:C1')
node3 = Node('node2', "192.168.1.2", 'C9:2A:4E:61:AD:F3')
print(Node.totalNodes())
