
from Enums.VehicleType import VehicleType

class Vehcle:
    def __init__(self, VehicleType):
        self.VehicleType = VehicleType
        
    def makeSound(self):
        print(f"{self.VehicleType} is starting")