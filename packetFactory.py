
from NSPyObject import NSPyObject
from packet import Packet


class PacketFactory(NSPyObject):

    _instance = None
    defaultSize = {"TCP": 2**10, "UDP": 2**9, "RTR": 2**8}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PacketFactory, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        pass

    def create(self, p_type: str, size=0) -> Packet:
        if p_type == "TCP":
            return Packet().type(p_type).size(size if size != 0 else PacketFactory.defaultSize.get(p_type))
        elif p_type == "UDP":
            return Packet().type(p_type).size(size if size != 0 else PacketFactory.defaultSize.get(p_type))
        elif p_type == "RTR":
            return Packet().type(p_type).size(size if size != 0 else PacketFactory.defaultSize.get(p_type))
