from modules.modules import Modules
from navigation import Navigation
from admin import SystemAdmin
import random
import string

class Vehicle:
    # Class attributes
    def __init__(self):
        self.localization, self.vehicle_control, self.perception, self.planning, self.system_management, self.sensor_fusion = Modules.get_modules()
        self.navigation = Navigation(self.localization)
        self.admin = SystemAdmin()
        self.sensor_data = self.sensor_fusion.get_sensor_data()
        self.speed = self.localization.get_speed()
        self.aww_status = False
        self.automation_level = 1
        self.id = ''.join(random.choices(string.ascii_lowercase, k=5))

    # Class methods
    def get_speed(self):
        return self.localization.get_speed()[0]

    def get_acceleration(self):
        return self.localization.get_acceleration()

    def get_orientation(self):
        return self.localization.get_orientation()

    def distance(self, battery):
        return self.battery_capacity * battery

    def get_battery_level(self):
        return self.battery_level

    def get_sensor_data(self):
        return self.sensor_data

    def set_headlights(self, level):
        self.light_level = level

    def set_wiper_level(self, wiper_level):
        self.wiper_level = wiper_level

    def get_obstacles(self):
        return self.sensor_data

    def get_obstacle_distance(self):
        pass

    def accelerate(self, amount):
        self.vehicle_control.accelerate(amount)

    def brake(self, amount):
        self.vehicle_control.brake(amount)

    def steer(self, direction):
        self.vehicle_control.steer(direction)

    def reset(self):
        self.vehicle_control.reset()

    def set_steer(self, angle):
        self.vehicle_control.set_steer(angle)

    def get_steer(self):
        return self.vehicle_control.get_steer()

    def decrease_speed(self):
        self.vehicle_control.decrease_speed(self.speed)

    def increase_speed(self):
        self.vehicle_control.increase_speed(self.speed)

    def set_windshield_wipers(self, lvl):
        self.vehicle_control.set_windshield_wipers(lvl)

    def get_windshield_wipers(self):
        return self.vehicle_control.get_windshield_wipers()

    def set_aww_status(self, rain_mph, status):
        print("Setting AWW status to: " + str(status))
        if status:
            level = self.planning.aww_status(rain_mph)
            self.vehicle_control.set_windshield_wipers(level)
        self.aww_status = status

    def get_aww_status(self):
        return self.aww_status

    def should_brake(self, obstacle_input):
        return self.planning.should_brake(obstacle_input)

    def set_destination(self, destination):
        self.navigation.set_destination(destination)

    def get_route(self):
        return self.navigation.get_route()

    def get_current_location(self):
        curr_location = self.navigation.get_current_location()
        print("Current Location: " + curr_location)
        return curr_location

    def update_system(self):
        self.admin.update_system()

    def shutdown_system(self):
        self.admin.shutdown_system

    def monitor_system(self):
        self.admin.monitor_system()

    def warn_battery_lvl(self, battery=50):
        self.admin.warn_battery_lvl(battery)

    def troubleshoot(self, issue):
        self.admin.troubleshoot(issue)

    def login(self, username, password):
        self.admin.login(username, password)

    def set_automation_level(self, level):
        level = min(level, 5)
        print("Setting automation level to: " + str(level))
        self.automation_level = level

    def get_automation_level(self):
        return self.automation_level

    def get_traffic_light_status(self):
        return self.perception.get_traffic_light_status()

    def get_signal_status(self):
        return self.perception.get_signal_status()

    def get_weather_status(self):
        return self.perception.get_weather()

    def get_light_level(self):
        return self.vehicle_control.get_light_level()

    def set_light_level(self, level):
        self.vehicle_control.set_light_level(level)
        
    def is_in_blindspot(self):
        self.planning.is_in_blindspot()
