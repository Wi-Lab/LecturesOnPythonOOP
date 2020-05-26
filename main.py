'''
Builder Pattern
'''


'''
Builder Pattern is a unique design pattern which helps in building complex object
 using simple objects and uses an algorithmic approach. 
'''


class Packet:
    def __init__(self, id, dst):
        self.id = id
        self.dst = dst


p1 = Packet(1, 'node1')
p2 = Packet(1, 'node2')
p3 = Packet(1, 'node3')
p4 = Packet(1, 'node4')
p5 = Packet(1, 'node5')
p6 = Packet(1, 'node6')
p7 = Packet(1, 'node7')

'''
what if we add a new property to our Packet class?
'''
