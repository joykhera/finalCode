import random


class Environment:
    def __init__(self, traffic_signs=[], obstacle_types=[], obstacle_locations=[], weather_conditions="sunny", road_conditions=1):
        self.traffic_signs = traffic_signs
        self.obstacle_types = obstacle_types
        self.obstacle_locations = obstacle_locations
        self.weather_conditions = weather_conditions
        self.road_conditions = road_conditions

    # Class methods
    def get_signals(self):
        # Code to get signals from other cars around
        directions = ['left', 'right', 'forward', 'backward']
        return "Car " + random.choice(directions)

    def get_lights(self):
        # Code to get the value of luminous flux around the car
        return random.randint(0, 2)

    def get_weather_conditions(self):
        return self.weather_conditions

    def get_road_network(self):
        # 0: no traffic, 1: light traffic, 2: heavy traffic
        return self.road_conditions

    def get_traffic_signals(self):
        # Code to get the current traffic signals status at each intersection
        return random.randint(0, 2)

    # def get_obstacles(self):
    #     # Code to get a list of the obstacles distance present in the environment
    #     pass

    # def get_obstacle_distance(self, obstacle):
    #     # Code to get the distance at which a given obstacle is in front of the car
    #     pass
