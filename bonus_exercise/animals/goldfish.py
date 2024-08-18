from .water_animal import WaterAnimal


class Goldfish(WaterAnimal):
    def eat(self):
        print("Goldfish is eating flakes.")

    def sleep(self):
        print("Goldfish is sleeping near the tank's bottom.")

    def swim_to(self):
        print("Goldfish swims to a safer place.")

    def hide_from_cat(self):
        print("Goldfish hides from the cat.")
