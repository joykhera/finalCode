import random

class VehicleControl:
    def __init__(self, planning, acceleration=1, braking=1, steering=1):
        self.planning = planning
        self.acceleration = acceleration
        self.braking = braking
        self.steering = steering
        self.windshield_wipers = random.randint(0, 5)
        self.light_level = random.randint(0, 5)

    def accelerate(self, amount):
        self.acceleration = amount

    def brake(self, amount):
        self.braking = amount

    def steer(self, direction):
        self.steering = direction

    def reset(self):
        self.acceleration = 0
        self.braking = 0
        self.steering = 0

    def set_steer(self, angle):
        self.steering = angle

    def get_steer(self):
        return self.steering

    def decrease_speed(self, speed):
        speed[0] -= 5

    def increase_speed(self, speed):
        speed[0] += 5

    def set_windshield_wipers(self, lvl):
        print("Current wiper speed: " + str(lvl))
        self.windshield_wipers = lvl

    def get_windshield_wipers(self):
        return self.windshield_wipers
    
    def get_light_level(self):
        return self.light_level
    
    def set_light_level(self, level):
        self.light_level = level
