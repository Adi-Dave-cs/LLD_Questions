from typing import List
from parking_spot import ParkingSpot
from vehicle import Vehicle
from vehicle_type import vehicle_type

class Level:
    def __init__(self,floor,num_spots):
        self.floor = floor
        self.parking_spots = [ParkingSpot(i,vehicle_type.CAR if i%3==0 else vehicle_type.BIKE if i%3==1 else vehicle_type.TRUCK) for i in range(num_spots)]
    
    def parkVehicle(self,vehicle:Vehicle):
        for spot in self.parking_spots:
            if(spot.isAvailable() and spot.get_type()==vehicle.get_type()):
                spot.parkVehicle(vehicle)
                return True
        return False
    
    def unparkVehicle(self,vehicle:Vehicle):
        for spot in self.parking_spots:
            if(not spot.isAvailable() and spot.get_parked_vehicle()==vehicle):
                spot.unparkVehicle()
                return True
        return False
    
    def display_availability(self):
        print(f"Level : {self.floor} Availability")
        for spot in self.parking_spots:
            print(f"Spot : {spot.get_spotNumber()} is {'Available' if spot.isAvailable() else 'Occupied'} ")