vehicles = []
class Communication:
        
    @staticmethod
    def remove_vehicle(vehicle):
        print("Removing vehicle from network: " + str(vehicle.id))
        vehicles.remove(vehicle)

    @staticmethod
    def add_vehicle(vehicle):
        print("Adding vehicle to network: " + str(vehicle.id))
        vehicles.append(vehicle)
        
    @staticmethod
    def get_vehicles():
        return vehicles
