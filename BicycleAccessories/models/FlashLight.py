from BicycleAccessories.models.BicycleAccessories import BicycleAccessories


class Flashlight(BicycleAccessories):
    def __init__(self,
                 name,
                 weight,
                 manufacturer,
                 producing_country,
                 types_manufacturer,
                 distance_of_lighting,
                 price):
        super().__init__(name, weight, manufacturer, producing_country,
                         types_manufacturer)
        self.distance_of_lighting = distance_of_lighting
        self.price = price

    def __str__(self):
        return super().__str__() \
               + "\nPrice:  " + str(self.price) \
               + "\nDistance of lighting:  " + str(self.distance_of_lighting)

    def __del__(self):
        pass
