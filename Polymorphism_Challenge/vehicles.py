# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")


# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")


# Subclass: Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴‍♂️")
