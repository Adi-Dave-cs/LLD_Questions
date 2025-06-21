from typing import List
from level import Level
from vehicle import Vehicle

class ParkingLot:
    _instance = None
    def __init__(self):
        if(not ParkingLot._instance):
            ParkingLot._instance=self
            self.levels :List[Level]= list()
        else:
            return Exception("This Class is a singleton class")
        
    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot()
        return ParkingLot._instance
    def add_level(self, level: Level) -> None:
        self.levels.append(level)

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.parkVehicle(vehicle):
                return True
        return False

    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.unparkVehicle(vehicle):
                return True
        return False

    def display_availability(self) -> None:
        for level in self.levels:
            level.display_availability()