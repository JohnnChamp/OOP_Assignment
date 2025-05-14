from vehicles import Car, Plane, Boat, Bicycle

# Create a list of vehicles
vehicles = [Car(), Plane(), Boat(), Bicycle()]

# Demonstrate polymorphism
for vehicle in vehicles:
    vehicle.move()
