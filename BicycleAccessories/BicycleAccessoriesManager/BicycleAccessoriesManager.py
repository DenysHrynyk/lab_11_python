class BicycleAccessoriesManager:

    def __init__(self, bicycle_accessories_list=()):
        self.bicycle_accessories_list = bicycle_accessories_list

    def sort_by_weight(self, bicycle_accessories_list, is_reversed):
        return sorted(bicycle_accessories_list, key=lambda bicycle_accessories: bicycle_accessories.weight,
                      reverse=is_reversed)

    def sort_by_types_manufacturer(self, bicycle_accessories_list, is_reversed):
        return sorted(bicycle_accessories_list,
                      key=lambda bicycle_accessories: repr(bicycle_accessories.types_manufacturer),
                      reverse=is_reversed)

    def find_by_manufacter(self, bicycle_accessories_list, type_of_manufacturer):
        return list(filter(lambda bicycle_accessories: bicycle_accessories.types_manufacturer == type_of_manufacturer,
                           bicycle_accessories_list))

    def __del__(self):
        pass
