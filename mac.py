from NSPyObject import NSPyObject
from osiLayer import OSILayer
from enum import Enum
from packet import Packet
from packet import PacketDir
from packet import PacketDirNotFoundException
from simulator import Simulator
from handler import Handler


class Duplexity(Enum):
    FULL = 1
    HALF = 2


class MacStatus(Enum):
    IDLE = 1
    RX = 2
    TX = 3
    RX_TX = 4


class MacRecvTxPacketInTxStateException(Exception):
    def __init__(self):
        self.message = "Mac received packet for transmission while it was in transmit state"
        super().__init__(self.message)


class MacRecvTxPacketInRxStateWithHalfDuplexException(Exception):
    def __init__(self):
        self.message = "Mac received packet for transmission while it was in recv state and has half duplex setting"
        super().__init__(self.message)


class MacRecvTxPacketInTxRxStateException(Exception):
    def __init__(self):
        self.message = "Mac received packet for transmission while it was in recv state and has half duplex setting"
        super().__init__(self.message)


class Mac(NSPyObject, OSILayer):
    '''This class models MAC layer'''

    def __init__(self):
        self._macStatus: MacStatus = MacStatus.IDLE

    def duplexity(self, duplexity: Duplexity) -> 'Mac':
        self._duplexity = duplexity
        return self

    def up(self, upTarget: OSILayer) -> 'Mac':
        self._upTarget = upTarget
        return self

    def down(self, downTarget: OSILayer) -> 'Mac':
        self._downTarget = downTarget
        return self

    def recv(self, packet: Packet):
        # Check packet direction first
        try:
            if packet._dir == PacketDir.DOWN:
                self.send(packet)
            elif packet._dir == PacketDir.UP:
                self._upTarget.recv(packet)
            else:
                raise PacketDirNotFoundException(packet.dir)
        except PacketDirNotFoundException as pe:
            print(pe)

    def send(self, packet: Packet):
        # we have recveivd a packet from upper layer
        # we need to check mac status first
        if self._macStatus == MacStatus.TX:
            # This is not a valid state
            raise MacRecvTxPacketInTxStateException()
        elif self._macStatus == MacStatus.RX:
            # we received a packet from upper layer, but we are currently receiving packet from down layer
            # we need to check duplexity settings
            if self._duplexity == Duplexity.HALF:
                # This is not a valid state
                raise MacRecvTxPacketInRxStateWithHalfDuplexException()
            else:  # mac has full duplex setting

                self._macStatus = MacStatus.RX_TX

                class PacketSendHandler(Handler):
                    def __init__(self, mac: 'Mac'):
                        self._mac = mac

                    def execute(self):
                        self._mac.sent(packet)
                Simulator().after(0.01, PacketSendHandler(self))
        elif self._macStatus == MacStatus.RX_TX:
            # this is not a valid state
            raise MacRecvTxPacketInRxStateWithHalfDuplexException()

        else:  # macStatus is IDLE
            self._macStatus = MacStatus.TX

            class PacketSendHandler(Handler):
                def __init__(self, mac: 'Mac'):
                    self._mac = mac

                def execute(self):
                    self._mac.sent(packet)
            Simulator().after(0.01, PacketSendHandler(self))

    def sent(self, packet: Packet):
        # packet has been sent
        self._downTarget.recv(packet)
        # we need to set macStatus
        if self._macStatus == MacStatus.RX_TX:
            self._macStatus = MacStatus.RX
        elif self._macStatus == MacStatus.TX:
            self._macStatus = MacStatus.IDLE
        # now we need to notify upper layer that we have sent packet
        packet._handler.execute()



# unit test
if __name__ == "__main__":
    pass
