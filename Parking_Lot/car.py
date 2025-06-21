from vehicle_type import vehicle_type
from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self,license_plate):
        super().__init__(license_plate,vehicle_type.CAR)
