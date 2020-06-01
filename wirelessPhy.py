from NSPyObject import NSPyObject
from osiLayer import OSILayer
from enum import Enum
from packet import Packet
from packet import PacketDir
from packet import PacketDirNotFoundException


class Duplexity(Enum):
    FULL = 1
    HALF = 2


class RadioStatus(Enum):
    IDLE = 1
    RX = 2
    TX = 3
    RX_TX = 4


class WirelessPhy(NSPyObject, OSILayer):
    '''This class models a wireless pyhisical layer'''

    def __init__(self):
        self._radioStatus: RadioStatus = RadioStatus.IDLE

    def duplexity(self, duplexity: Duplexity) -> 'WirelessPhy':
        self._duplexity = duplexity
        return self

    def up(self, upTarget: OSILayer) -> 'WirelessPhy':
        self._upTarget = upTarget
        return self

    def down(self, downTarget: OSILayer) -> 'WirelessPhy':
        self._downTarget = downTarget
        return self

    def recv(self, packet: Packet):
        # Check packet direction first
        try:
            if packet._dir == PacketDir.DOWN:
                print(f"delivered packet <{packet._uid}> to channel")
            elif packet._dir == PacketDir.UP:
                self._upTarget.recv(packet)
            else:
                raise PacketDirNotFoundException(packet.dir)
        except PacketDirNotFoundException as pe:
            print(pe)



# unit test
if __name__ == "__main__":
    from packetFactory import PacketFactory as pf
    from packet import PacketType
    phy = WirelessPhy().duplexity(Duplexity.FULL)
    p = pf().create(PacketType.TCP).dir("ssss")
    phy.recv(p)
