from BicycleAccessories.models.BicycleAccessories import BicycleAccessories


class BicycleComputer(BicycleAccessories):
    def __init__(self, name, weight, manufacturer, producing_country,
                 types_manufacturer, display_widening, battery, mounting_method, navigator):
        super().__init__(name, weight, manufacturer, producing_country, types_manufacturer)
        self.display_widening = display_widening
        self.battery = battery
        self.mounting_method = mounting_method
        self.navigator = navigator

    def __str__(self):
        return super().__str__() \
               + "\nDisplay widening:  " + str(self.display_widening) \
               + "\nBattery:  " + str(self.battery) \
               + "\nMounting method:  " + self.mounting_method \
               + "\nNavigator: " + str(self.navigator)

    def __del__(self):
        pass
