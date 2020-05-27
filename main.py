'''
Factory Pattern
'''


class Packet:
    def __init__(self):
        pass

    def type(self, type):
        self._type = type
        return self

    def id(self, id):
        self.id = id
        return self

    def dst(self, dst):
        self.dst = dst
        return self


p1 = Packet().id(1).dst("node1").type("MAC")
