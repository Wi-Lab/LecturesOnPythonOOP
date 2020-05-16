'''
Accessing object attributes
'''


class Node:
    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac


n1 = Node('192.168.1.2', 'C9:2A:4E:61:AD:C7')
n2 = Node('192.168.1.3', 'C9:2A:4E:61:AD:C8')

print("Node n1 with IP<{}> and MAC<{}>".format(n1.ip, n1.mac))
print("Node n2 with IP<{}> and MAC<{}>".format(n2.ip, n2.mac))
