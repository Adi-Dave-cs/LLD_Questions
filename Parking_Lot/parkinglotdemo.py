from ParkingLot import ParkingLot
from level import Level
from car import Car
from bike import bike
from Truck import Truck

class ParkingLotDemo:
    def run():
        parking_lot = ParkingLot.get_instance()
        parking_lot.add_level(Level(1, 5))
        parking_lot.add_level(Level(2, 4))

        car = Car("ABC123")
        truck = Truck("XYZ789")
        motorcycle = bike("M1234")

        # Park vehicles
        parking_lot.park_vehicle(car)
        parking_lot.park_vehicle(truck)
        parking_lot.park_vehicle(motorcycle)

        # Display availability
        parking_lot.display_availability()

        # Unpark vehicle
        parking_lot.unpark_vehicle(motorcycle)

        # Display updated availability
        parking_lot.display_availability()

if __name__ == "__main__":
    ParkingLotDemo.run()