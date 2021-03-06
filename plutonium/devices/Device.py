from plutonium.interfaces.Interface import Interface


class Device:
    def __init__(self, sensors: list, interface: Interface):
        self.sensors = sensors
        self.interface = interface

    def standby(self):
        raise NotImplementedError()

    def activate(self):
        raise NotImplementedError()

    def reset(self):
        raise NotImplementedError()
