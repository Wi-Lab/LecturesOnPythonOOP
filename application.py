from NSPyObject import NSPyObject
from osiLayer import OSILayer
from packet import Packet
from packet import PacketDir
from handler import Handler
from simulator import Simulator
from packetFactory import PacketFactory as pf
from packet import PacketType


class PacketWithDownDirectionInAppLayerException(Exception):
    def __init__(self, p: Packet):
        self.message = f"packet with id <{p._uid}> has wrong direction in Application Layer"
        super().__init__(self.message)


class Application(NSPyObject, OSILayer):

    def __init__(self, rate: int):
        self._running = False
        self._rate = rate

    def recv(self, packet: Packet):
        # Check packet direction first
        try:
            if packet._dir == PacketDir.UP:
                print(packet)
                del packet
            else:
                raise PacketWithDownDirectionInAppLayerException(packet.dir)
        except PacketWithDownDirectionInAppLayerException as pe:
            print(pe)

    def down(self, downTarget: OSILayer) -> 'Application':
        self._downTarget = downTarget
        return self

    def start(self, at: float):
        self._running = True
        Simulator().at(at, Application.GenerateNewDataHandler(self))

    def stop(self, at: float):
        Simulator().at(at, Application.StopDataGenerationHandler(self))

    class GenerateNewDataHandler(Handler):
        def __init__(self, application: 'Application'):
            self._app = application

        def execute(self):
            if __name__ == "__main__":
                print(f"Generating new data at {Simulator().now()}")
            else:
                self._app._downTarget.recv(pf().create(PacketType.UDP))
            # we need to schedule for next data generation
            if self._app._running is True:
                Simulator().after(1.0/self._app._rate, Application.GenerateNewDataHandler(self._app))

    class StopDataGenerationHandler(Handler):
        def __init__(self, application: 'Application'):
            self._app = application

        def execute(self):
            self._app._running = False


if __name__ == "__main__":
    app = Application(100)
    app.start(1.0)
    app.stop(100.0)
    Simulator().run()
