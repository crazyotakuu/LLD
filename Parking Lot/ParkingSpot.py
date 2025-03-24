class ParkingSpot:
    def __init__(self, spot_no,vehicle=None, vehicle_type):
        self.spot_no=spot_no
        self.vehicle=None
        self.vehicle_type=vehicle_type
    def park_vehicle(self, vehicle):
        self.vehicle=vehicle
    def unpark_vehicle(self):
        self.vehicle=None