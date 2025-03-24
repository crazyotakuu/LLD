from abc import ABC, abstractmethod
class VehicleType:
    def __init__(self):
        self.vehicle_no=None
        self.vehicle_type=None
    @abstractmethod
    def pay(self):
        pass