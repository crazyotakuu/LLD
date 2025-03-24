class Truck(VehicleType):
    def __init__(self, vehicle_no):
        self.vehicle_no=vehicle_no
        self.vehicle_type="Truck"

    def pay(self):
        print(f"Paying for vehicle no:{self.vehicle_no}")