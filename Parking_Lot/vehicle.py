from abc import ABC
from vehicle_type import vehicle_type

class Vehicle(ABC):
    def __init__(self, license_plate:str , vehicle_type:vehicle_type):
        self.license_number = license_plate
        self.type = vehicle_type
    
    def get_type(self):
        return self.type