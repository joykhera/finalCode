import random


class Planning:

    def __init__(self, sensor_fusion):
        self.sensor_fusion = sensor_fusion

    def should_brake(self, obstacle_input):
        result = 100 > obstacle_input
        print("Should brake: " + str(result))
        return result

    def should_merge(self, speed, vehicle_input):
        temp = speed < vehicle_input
        print('should merge' + temp)
        return temp

    def should_turn(self, speed, vehicle_input):
        temp = speed < vehicle_input
        print('should turn' + temp)
        return temp

    def should_accelerate(self, speed, vehicle_input):
        temp = speed < vehicle_input
        print('should accelerate' + temp)
        return temp

    def should_decelerate(self, speed, vehicle_input):
        temp = speed < vehicle_input
        print('should deccelerate' + temp)
        return temp

    def aww_status(self, rain_speed):
        wiper_speed = rain_speed/10 if rain_speed/10 <= 5 else 5
        return wiper_speed

    def is_in_blindspot(self):
        blindspot_status = random.choice(self.sensor_fusion.sensor_data['blindspot_images'])
        if blindspot_status == 0:
            print("Object detected in left vehicle blindspot. Vehicle will not merge left")
        elif blindspot_status == 1:
            print("Object detected in right vehicle blindspot. Vehicle will not merge right")
        else:
            print("No objects in blindspots. Vehicle may merge right or left")
