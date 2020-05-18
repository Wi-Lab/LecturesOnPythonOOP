'''
Inheritance
    - Inheritance is the process by which one class takes on the attributes 
      and methods of another.
    - Newly formed classes are called child classes.

    - The classes that child classes are derived from are called parent classes.

    - Child classes inherit all of the parent’s attributes and behaviors 
      but can also specify different behavior to follow.

    - The most basic type of class is an object, which generally all other classes 
      inherit as their parent.

'''

'''
class Node(object):
    pass

# In Python 3, this is the same as:

class Node:
    pass
'''


class Node:
    def __init__(self, name, ip, mac):
        self.name = name  # Public
        self._ip = ip    # protected
        self._mac = mac  # private
        self.__queue = []  # private

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


# WirelessNode inherites all attributes and methods of Node class
class WirelessNode(Node):
    def __init__(self, name, ip, mac, radio_range):
        super().__init__(name, ip, mac)
        self.radio_range = radio_range  # Public

    # overriding instance method of parent class
    def description(self):
        return "WN <{}>, IP<{}>, MAC<{}>,RR<{}>".format(self.name, self._ip, self._mac, self.radio_range)

    def getRadioRange(self):
        return "RR of <{}> is <{}> meters.".format(self.name, self.radio_range)


n1 = WirelessNode('node 1', '192.168.1.2', 'C9:2A:4E:61:AD:C7', 10)
n2 = Node('node 2', '192.168.1.3', 'C9:2A:4E:61:AD:C8')

print(n1.description())
print(n2.description())
