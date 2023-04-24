from communication import Communication
from vehicle import Vehicle
vehicle = Vehicle()

# 7. Testing

# 7.1 Scenario-Based Testing(based on 4.1 / 4.2 Use-Cases)

# 7.1.1 Driver Turns on AWW
# rain_mph = 40
# vehicle.set_aww_status(rain_mph, True)
# print()
# vehicle.set_aww_status(20, False)


# 7.1.2 Vehicle Auto-Brakes When an Obstacle is in Front
# obstacle_distance = 10
# vehicle.should_brake(obstacle_distance)
# print()
# obstacle_distance = 110
# vehicle.should_brake(obstacle_distance)

# 7.1.3 Vehicle Decides Route Based on Current Location and Destination from Connected Cell Phone
# vehicle.get_current_location()
# print()
# vehicle.set_destination("123 Main St")

# 7.1.4 Alset Wants to Install a Software Update
# vehicle.update_system()

# 7.1.5 Object is Detected in Blindspot of Vehicle
# vehicle.is_in_blindspot()

# 7.2 Validation Testing(based on 3.1 Requirements)

# 7.2.1 Auto-Brake for In Front
# vehicle.should_brake(10)

# 7.2.2 Changing Automation Level
# vehicle.set_automation_level(2)

# 7.2.3 Traffic Light Recognition
print("Status: " + vehicle.get_traffic_light_status())

# 7.2.4 Signal Recognition
# print("Signal Recognition: " + str(vehicle.get_signal_status()))

# 7.2.5 Weather Recognition
# print("Weather Recognition: " + str(vehicle.get_weather_status()))

# 7.2.6 Automatic Lighting
# print("Light Level: " + str(vehicle.get_light_level()))

# 7.2.7 Headlight Control
# print("Light Level: " + str(vehicle.get_light_level()))

# 7.2.8 Blind Spot Detection
# vehicle.is_in_blindspot()

# 7.2.9 Speed Control
# print("Current speed of the vehicle: " + str(vehicle.get_speed()) + " mph")
# vehicle.increase_speed()
# print("Current speed of the vehicle: " + str(vehicle.get_speed()) + " mph")
# vehicle.decrease_speed()
# print("Current speed of the vehicle: " + str(vehicle.get_speed()) + " mph")

# 7.2.10 Vehicle Infrastructure and Connection Network
# print(Communication.get_vehicles())
# Communication.add_vehicle(vehicle)
# print(Communication.get_vehicles())
# Communication.remove_vehicle(vehicle)
# print(Communication.get_vehicles())
