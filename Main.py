from BicycleAccessories.Enums.TypesManufacturer import TypesManufacturer
from BicycleAccessories.models.BicycleComputer import BicycleComputer
from BicycleAccessories.models.FlashLight import Flashlight
from BicycleAccessories.BicycleAccessoriesManager.BicycleAccessoriesManager import BicycleAccessoriesManager
from BicycleAccessories.Enums.Navigator import Navigator
from BicycleAccessories.Enums.ProducingCountry import ProducingCountry
from BicycleAccessories.models.Speedometer import Speedometer
from BicycleAccessories.Enums.DistanceOfLighting import DistanceOfLighting
from BicycleAccessories.Enums.SpedometerType import SpeedometerType


def main():
    manager = BicycleAccessoriesManager()
    flashlight = Flashlight("k4000", 125, "Shimano", ProducingCountry.CHINA, TypesManufacturer.GARMIN,
                            DistanceOfLighting.MIDDLE, 75)
    bicycle_computer = BicycleComputer("Sd200", 200, "Infini", ProducingCountry.EUROPE, TypesManufacturer.SHIMANO,
                                       DistanceOfLighting.LONG, 1200, "doc", Navigator.OFFLINE)
    speedometer = Speedometer("F200", 1200, "Garmin", ProducingCountry.EUROPE, TypesManufacturer.INFINI, 250,
                              SpeedometerType.ELECTRONIC)

    bicycle_accessories_list = [flashlight, bicycle_computer, speedometer]

    print(*manager.sort_by_types_manufacturer(bicycle_accessories_list, True))

    print(*manager.sort_by_weight(bicycle_accessories_list, True))

    print(*manager.find_by_manufacter(bicycle_accessories_list, TypesManufacturer.GARMIN))


if __name__ == '__main__':
    main()
