from vehicle import Vehicle
from vehicle_type import vehicle_type

class ParkingSpot:
    def __init__(self,spot_number,vehicle_type):
        self.spot_number = spot_number
        self.type = vehicle_type
        self.parked = None
    
    def isAvailable(self) -> bool:
        return self.parked == None
    
    def parkVehicle(self,vehicle:Vehicle) -> None:
        if(self.isAvailable() and self.get_type()==vehicle.get_type()):
            self.parked = vehicle
        else:
            raise ValueError("InValid vehicle spot occupied!")
        return True
    
    def unparkVehicle(self) -> None:
        self.parked = None
        return
    
    def get_spotNumber(self) -> int:
        return self.spot_number
    
    def get_type(self) -> vehicle_type:
        return self.type
    
    def get_parked_vehicle(self) -> Vehicle:
        return self.parked