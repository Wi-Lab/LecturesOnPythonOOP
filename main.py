'''
Instance Methods
'''


class Node:
    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac

    # instance method
    def description(self):
        return "Node n1 with IP<{}> and MAC<{}>".format(self.ip, self.mac)

    # instance method
    def sendPacket(self, payload, dst):
        return "Sending {} to node {}".format(payload, dst.ip)


n1 = Node('192.168.1.2', 'C9:2A:4E:61:AD:C7')
n2 = Node('192.168.1.3', 'C9:2A:4E:61:AD:C8')

print(n1.description())

print(n2.sendPacket("MESSAGE", n1))
