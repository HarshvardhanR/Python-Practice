
from ParkingLot.Enums.vehicle_type import VehicleType

class Vehicle:
    def __init__(self, VehicleType):
        self.VehicleType = VehicleType
        
    def makeSound(self):
        print(f"{self.VehicleType} is starting")