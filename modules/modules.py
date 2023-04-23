from modules.localization import Localization
from modules.sensor_fusion import SensorFusion
from modules.perception import Perception
from modules.planning import Planning
from modules.system_management import SystemManagement
from modules.vehicle_control import VehicleControl


class Modules:

    @staticmethod
    def get_modules():
        localization = Localization()
        perception = Perception()
        sensor_fusion = SensorFusion(localization, perception)
        planning = Planning(sensor_fusion)
        system_management = SystemManagement()
        vehicle_control = VehicleControl(planning)
        return localization, vehicle_control, perception, planning, system_management, sensor_fusion
