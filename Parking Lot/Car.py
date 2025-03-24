class Car(VehicleType):
    def __init__(self, vehicle_no):
        self.vehicle_no=vehicle_no
        self.vehicle_type="Car"

    def pay(self):
        print(f"Paying for vehicle no:{self.vehicle_no}")