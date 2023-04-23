from vehicle import Vehicle
from admin import SystemAdmin
from environment import Environment

print("Main class initialized")
# Create instances of classes
vehicle = Vehicle()
system_admin = SystemAdmin()
environment = Environment()

# Use the classes
vehicle.increase_speed(vehicle.speed)
print(f"Current speed of the vehicle: {vehicle.get_speed()} mph")
assert vehicle.planning.should_brake(10)

system_admin.login("admin", "password")
system_admin.update_system()

navigation = vehicle.navigation
navigation.set_destination("123 Main St")
print(f"Planned route: {navigation.get_planned_route()}")
