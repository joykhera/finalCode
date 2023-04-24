import random


class Perception():
    def __init__(self):
        self.camera = Camera()
        self.lidar = Lidar()

    def set_lidar(self, lidar):
        self.lidar = lidar

    def get_camera_images(self):
        images = []
        images.append(self.camera.take_image())
        return images

    def get_lidar_data(self):
        return self.lidar.scan()

    def blindspot(self):
        return self.camera.blindspot()

    def get_traffic_light_status(self):
        return random.randint(0, 2)

    def get_signal_status(self):
        return random.getrandbits(1)

    def get_weather(self):
        return self.camera.get_weather()


class Camera:
    image_taken = False
    image = ""

    def __init__(self):
        self.resolution = (1920, 1080)

    def take_image(self):
        self.image_taken = True
        self.image = "Image taken"
        pass

    def get_image(self):
        if self.image_taken:
            return self.image

    def blindspot(self):
        # info from 4 blindspot cameras
        return [0, 1, 2]

    def get_weather(self):
        return random.choice(["sunny", "rainy", "snowy", "foggy", "windy", "cloudy", "clear"])


class Lidar:
    def __init__(self):
        self.scan_resolution = 0.1

    def scan(self):
        # Code for Lidar scanning
        return "Lidar scan"
