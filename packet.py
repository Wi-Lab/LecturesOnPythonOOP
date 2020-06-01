
from NSPyObject import NSPyObject
from enum import Enum
from handler import Handler


class PacketType(Enum):
    TCP = 1
    UDP = 2
    RTR = 3


class PacketDir(Enum):
    UP = 1
    DOWN = 2
    UNKNOWN = 3


class PacketDirNotFoundException(Exception):
    """Exception raised for wrong packet direction.

    Attributes:
        input dir
    """

    def __init__(self, p_dir):
        self.message = f"{p_dir} is not a valid packet direction"
        super().__init__(self.message)


class Packet(NSPyObject):
    packetCount = 0

    def __init__(self):
        self._uid = Packet.packetCount
        Packet.packetCount += 1
        self._dir = PacketDir.DOWN  # most of the time we will create packets in application layer, so the direction is down

    def type(self, type: PacketType) -> 'Packet':
        self._type = type
        return self

    def size(self, size: int) -> 'Packet':
        self._size = size
        return self

    def dir(self, dir: PacketDir) -> 'Packet':
        self._dir = dir
        return self

    def handler(self, handler: Handler) -> 'Packet':
        self._handler = handler
        return self

    def __str__(self):
        print(f"P  <{self._uid}> <{self._type}> <{self._size}>")
