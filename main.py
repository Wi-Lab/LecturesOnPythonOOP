'''
Factory Pattern
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

    def crc(self, crc):
        self.crc = crc
        return self

    def fragmentId(self, fragmentId):
        self.fragmentId = fragmentId
        return self

    def fragmentCount(self, fragmentCount):
        self.fragmentCount = fragmentCount
        return self

    def timestamp(self, timestamp):
        self.timestamp = timestamp
        return self


p1 = Packet().id(1).dst("node1").crc("FA").fragmentId(1).fragmentCount(3).timestamp(0)
p2 = Packet().id(2).dst("node2")
p3 = Packet().id(3).dst("node3").crc("FA").fragmentId(1).fragmentCount(4).timestamp(0)
p4 = Packet().id(4).dst("node4")
p5 = Packet().id(5).dst("node5")
p6 = Packet().id(6).dst("node6")
