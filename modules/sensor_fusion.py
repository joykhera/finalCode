class SensorFusion():
    def __init__(self, localization, perception):
        self.localization = localization
        self.perception = perception
        self.sensor_data = self.get_sensor_data()

    def get_sensor_data(self):
        """
        Combines sensor data from all sensors into a single object for the Planning and Vehicle Control modules.
        """
        sensor_data = {}

        # Get GPS/IMU data
        sensor_data['location'] = self.localization.get_location()
        sensor_data['speed'] = self.localization.get_speed()
        sensor_data['acceleration'] = self.localization.get_acceleration()
        sensor_data['orientation'] = self.localization.get_orientation()

        # Get camera data
        sensor_data['camera_images'] = self.perception.get_camera_images()
        sensor_data['blindspot_images'] = self.perception.blindspot()

        # Get LiDAR data
        sensor_data['lidar_image'] = self.perception.get_lidar_data()
        sensor_data['weather'] = self.perception.get_weather()
        return sensor_data
