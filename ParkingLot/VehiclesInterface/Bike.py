from VehiclesInterface.vehicle import Vehicle
from ParkingLot.Enums.vehicle_type import VehicleType

class Bike(Vehicle):
    def __init__(self):
        super().__init__(VehicleType.BIKE)