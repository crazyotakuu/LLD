from collections import deque
class ParkingLevel:
    def __init__(self, level_id):
        self.level_id=level_id
        self.available_spots={}
        self.occupied_spots={}
    def add_spot(self, spot):
        if spot.vehicle_type in available_spots:
            available_spots[spot.vehicle_type].append(spot)
        else:
            available_spots[spot.vehicle_type]=deque().append(spot)
    def park_vehicle(self, vehicle):
        parking_spot=self.available_spots[vehicle.vehicle_type].popleft()
        parking_spot.park_vehicle(vehicle)
        occupied_spots[vehicle.vehicle_no]=parking_spot
    def unpark_vehicle(self, vehicle):
        parking_spot=occupied_spots[vehicle.vehicle_no]
        parking_spot.unpark_vehicle()
        available_spots[parking_spot.vehicle_type].append(parking_spot)
    def display_availability(self):
        print(f"Availability in {self.level_id} leve")
        for i in self.available_spots.keys():
            print(f"{i} parking: {available_spots[i].len()}")