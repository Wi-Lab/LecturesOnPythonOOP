
from NSPyObject import NSPyObject


class Packet(NSPyObject):
    packetCount = 0

    def __init__(self):
        self._uid = Packet.packetCount
        Packet.packetCount += 1

    def type(self, type: str) -> 'Packet':
        self._type = type
        return self

    def size(self, size: int) -> 'Packet':
        self._size = size
        return self
