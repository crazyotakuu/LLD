class ParkingLot:
    _instance=None
    def __new__(cls, *args, *kwargs):
        if cls._instance is None:
            cls._instance=super.__new__(cls)
        return cls._instance
    def __init__(self):
        self.levels=[]
    def add_levels(self, level):
        if level:
            self.levels.appened(level)
        else:
            raise exception("Attribute Error: Can't append None to Levels")
    def park_vehicle(self, vehicle):
        for i in self.levels:
            i.park_vehicle(vehicle)
    def unpark_vehicle(self, vehicle):
        for i in self.levels:
            i.unpark_vehicle(vehicle)
    def display_availability(self):
        for level in self.levels:
            print(level.print_availability)
