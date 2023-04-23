
class Navigation():
    # Class attributes
    
    def __init__(self, localization):
        self.localization = localization
        self.route = self.localization.get_route()

    # Class methods
    def get_current_location(self):
        return self.localization.get_location()

    def get_route(self):
        return self.route

    def set_destination(self, destination):
        print('setting destination to ' + destination)
        # Code to set the destination for the car
        self.route = destination
