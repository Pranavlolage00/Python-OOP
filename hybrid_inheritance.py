class Vehicle:
    def move(self):
        print("Vehicle moves")


class Car(Vehicle):
    def drive(self):
        print("Car drives")


class Boat(Vehicle):
    def sail(self):
        print("Boat sails")


class AmphibiousVehicle(Car, Boat):
    def amphibious_action(self):
        print("Amphibious vehicle can both drive and sail")


amphibious_vehicle = AmphibiousVehicle()
amphibious_vehicle.move()
amphibious_vehicle.drive()
amphibious_vehicle.sail()
amphibious_vehicle.amphibious_action()
