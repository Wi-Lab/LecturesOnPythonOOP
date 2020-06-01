from abc import ABC, abstractmethod
from packet import Packet


class OSILayer(ABC):
    @abstractmethod
    def recv(self, packet: Packet):
        raise NotImplementedError


if __name__ == "__main__":
    pass
    # o = OSILayer()  # this statement will generate an error because OSILayer is an abstract class
