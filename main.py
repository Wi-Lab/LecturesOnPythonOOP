'''
Access Modifiers

Private members:
    Private members of a class are denied access from the environment outside the class.

Public members:
    Public members are accessible from outside the class.

Protected members:
    Protected members of a class are accessible from within the class and are also 
    available to its sub-classes.

*** All members in a Python class are public by default.


'''


class Node:
    def __init__(self, name, ip, mac):
        self.name = name  # Public
        self._ip = ip    # protected
        self.__mac = mac  # private
        self.__queue = []  # private

    # instance method
    def description(self):
        return "Node <{}> with IP<{}> and MAC<{}>".format(self.name, self._ip, self.__mac)

    # instance method
    def sendPacket(self, payload, dst):
        return "Sending {} to node {}".format(payload, dst._ip)

    # instance method that modifies attributes of instance
    def receivePacket(self, newPacket):
        self.queue.append(newPacket)

    def queueLength(self):
        return "Queue length is {}".format(len(self.__queue))


n1 = Node('node 1', '192.168.1.2', 'C9:2A:4E:61:AD:C7')
n2 = Node('node 2', '192.168.1.3', 'C9:2A:4E:61:AD:C8')

print(n1.description())

print(n1.name)

print(n1._ip)

print(n1.__mac)

# print(n1._Node__mac)
