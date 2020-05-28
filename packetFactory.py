
from NSPyObject import NSPyObject
from packet import Packet
from packet import PacketType


class PacketTypeNotFoundError(Exception):
    """Exception raised for wrong packet type.

    Attributes:
        input type 
    """

    def __init__(self, p_type):
        self.message = f"{p_type} is not a valid packet type"
        super().__init__(self.message)


class PacketFactory(NSPyObject):

    _instance = None
    defaultSize = {PacketType.TCP: 2**10, PacketType.UDP: 2**9, PacketType.RTR: 2**8}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PacketFactory, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        pass

    def create(self, p_type: PacketType, size=0) -> Packet:
        try:
            if p_type == PacketType.TCP:
                return Packet().type(PacketType.TCP).size(size if size != 0 else PacketFactory.defaultSize.get(PacketType.TCP))
            elif p_type == PacketType.UDP:
                return Packet().type(PacketType.UDP).size(size if size != 0 else PacketFactory.defaultSize.get(PacketType.UDP))
            elif p_type == PacketType.RTR:
                return Packet().type(PacketType.RTR).size(size if size != 0 else PacketFactory.defaultSize.get(PacketType.RTR))
            raise PacketTypeNotFoundError(p_type)
        except PacketTypeNotFoundError as e:
            print(e)
