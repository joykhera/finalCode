import random


class SystemAdmin:
    # Class attributes
    username = "Alset"
    password = "Alset"
    system_logs = []
    system_version = ""

    # Class methods
    def update_system(self):
        # Code to update the system
        rand = random.randint(1, 100)
        if rand <= 80:
            print("System updated successfully.")
        else:
            print("You have a virus.")

    def shutdown_system(self):
        # Code to safely shut down the system
        print("System shutdown successfully.")

    def monitor_system(self):
        # Code to monitor the system and record any issues in the system logs
        rand = random.randint(1, 100)
        if rand <= 95:
            print("System running smoothly.")
        else:
            print("Full system repair required. Make appointment with Alset.")

    def warn_battery_lvl(self, battery=50):
        if battery < 10:
            print("WARNING: Battery level is low.")
        else:
            print('Battery level is normal.')

    def troubleshoot(self, issue):
        # Code to troubleshoot the reported issue and make necessary updates/changes to the system
        print('Troubleshooting...')

    def login(self, username, password):
        if self.username == username and self.password == password:
            print("Login successful.")
        else:
            print("Invalid username or password.")
