from NSPyObject import NSPyObject
from osiLayer import OSILayer
from enum import Enum
from packet import Packet
from packet import PacketDir
from packet import PacketDirNotFoundException
from simulator import Simulator
from handler import Handler


class QueueState(Enum):
    EMPTY = 1
    NOT_EMPTY = 2
    FULL = 3


class DownTargetStatus(Enum):
    IDLE = 1
    BUSY = 2


class Queue(NSPyObject, OSILayer):
    '''This class models a Queue layer'''

    def __init__(self, size):
        self._size = size
        self._len = 0
        self._buffer = []
        self._downTargetStatus = DownTargetStatus.IDLE

    # In Queue object we do not need up target

    def down(self, downTarget: OSILayer) -> 'Queue':
        self._downTarget = downTarget
        return self

    def recv(self, packet: Packet):
        if self._downTargetStatus == DownTargetStatus.IDLE:
            # down target is IDLE we need to pass this packet to it
            # we need to set handler of this packet , so down target can notify us when he finished his job
            class DownTargetNeedsPacketHandler(Handler):
                def __init__(self, queue: 'Queue'):
                    self._queue = queue

                def execute(self):
                    if self._queue._len > 0:  # we have packet in queue
                        p: Packet = self._queue._buffer.pop(0)
                        self._queue._len -= 1
                        p.handler(DownTargetNeedsPacketHandler(self._queue))
                        self._downTargetStatus = DownTargetStatus.BUSY
                        self._queue._downTarget.recv(p)
                    else:  # we do not have packet in queue
                        self._queue._downTargetStatus = DownTargetStatus.IDLE

            packet.handler(DownTargetNeedsPacketHandler(self))
            # we need to set downtargetStatus to busy
            self._downTargetStatus = DownTargetStatus.BUSY
            self._downTarget.recv(packet)

        else:  # s elf._downTargetStatus != DownTargetStatus.IDLE:
          # downtargetStatus is busy we need to add this packet to queue
            if self._len <= self._size:
                # we have space to store this packet
                self._buffer.append(packet)
                self._len += 1
            else:
                # queue is full, so overflow will happen
                print(f"OverFlow in Queue packet {packet._uid} dropped")
                del packet



# unit test
if __name__ == "__main__":
    pass
