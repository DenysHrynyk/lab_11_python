from BicycleAccessories.models.BicycleAccessories import BicycleAccessories


class Speedometer(BicycleAccessories):
    def __init__(self, name, weight, manufacturer, producing_country,
                 types_manufacturer, size, speedometer_types):
        super().__init__(name, weight, manufacturer, producing_country, types_manufacturer)
        self.size = size
        self.speedometer_types = speedometer_types

    def __str__(self):
        return super().__str__()\
                + "\nSize: " + str(self.size)\
                + "\nSpeedometer of types: " + str(self.speedometer_types)

    def __del__(self):
        pass
