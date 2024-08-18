from .water_animal import WaterAnimal


class Whale(WaterAnimal):
    def eat(self):
        print("Whale is eating krill.")

    def sleep(self):
        print("Whale is sleeping while moving slowly.")

    def swim_to(self):
        print("Whale swims in the deep ocean.")

    def chase_sailboats(self):
        print("Whale chases sailboats.")
