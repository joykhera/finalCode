import math
import random

class Localization():
    def __init__(self):
        self.gps = GPS()
        self.imu = IMU()

    def get_location(self):
        """Returns the current location of the car."""
        return self.gps.get_location()

    def get_orientation(self):
        """Returns the current orientation of the car."""
        return self.imu.get_orientation()

    def get_speed(self):
        """Returns the current speed of the car."""
        return self.imu.get_speed()

    def get_acceleration(self):
        """Returns the current acceleration of the car."""
        return self.imu.get_acceleration()

    def get_route(self):
        """
        Sends a request to the server side application to receive the route to the
        destination, and returns it as a list of waypoints.
        """
        return self.gps.get_route()

    def calculate_distance(self, location1, location2):
        """
        Calculates the distance between two locations using the Haversine formula.
        """
        lat1, lon1 = location1
        lat2, lon2 = location2
        R = 6371  # radius of the earth in km
        dLat = math.radians(lat2 - lat1)
        dLon = math.radians(lon2 - lon1)
        a = math.sin(dLat/2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dLon/2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = R * c
        return distance


class GPS:
    def __init__(self, curr_location="UCC Towers"):
        self.curr_location = curr_location
        self.route = 'route'

    def get_location(self):
        return self.curr_location

    def get_route(self):
        return self.route

    def set_destination(self, destination):
        self.route = destination


class IMU:
    def __init__(self, speed=[1], acceleration=1, orientation=1):
        self.speed = speed
        self.acceleration = acceleration
        self.orientation = orientation

    def get_acceleration(self):
        return self.acceleration

    def get_orientation(self):
        return self.orientation

    def get_speed(self):
        """Returns the current speed of the car."""
        return self.speed
