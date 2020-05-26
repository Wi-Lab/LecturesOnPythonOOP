'''
Builder Pattern
'''


'''
Builder Pattern is a unique design pattern which helps in building complex object
 using simple objects and uses an algorithmic approach. 
'''


class Packet:
    def __init__(self):
        pass

    def id(self, id):
        self.id = id
        return self

    def dst(self, dst):
        self.dst = dst
        return self


p1 = Packet().id(1).dst("node1")
p2 = Packet().id(2).dst("node2")
p3 = Packet().id(3).dst("node3")
p4 = Packet().id(4).dst("node4")
p5 = Packet().id(5).dst("node5")
p6 = Packet().id(6).dst("node6")
