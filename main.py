'''
Instantiating Objects:
    Instantiating is a fancy term for creating a new, unique instance of a class.
'''


class Node:
    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac


n1 = Node('192.168.1.2', 'C9:2A:4E:61:AD:C7')
n2 = Node('192.168.1.3', 'C9:2A:4E:61:AD:C8')

print(n1 == n2)
