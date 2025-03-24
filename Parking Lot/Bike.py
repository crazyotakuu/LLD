class Bike(VehicleType):
    def __init__(self, vehicle_no):
        self.vehicle_no=vehicle_no
        self.vehicle_type="Bike"

    def pay(self):
        print(f"Paying for vehicle no:{self.vehicle_no}")