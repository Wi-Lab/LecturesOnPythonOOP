
from NSPyObject import NSPyObject
from enum import Enum


class PacketType(Enum):
    TCP = 1
    UDP = 2
    RTR = 3


class Packet(NSPyObject):
    packetCount = 0

    def __init__(self):
        self._uid = Packet.packetCount
        Packet.packetCount += 1

    def type(self, type: PacketType) -> 'Packet':
        self._type = type
        return self

    def size(self, size: int) -> 'Packet':
        self._size = size
        return self
