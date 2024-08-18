from .land_animal import LandAnimal


class Hamster(LandAnimal):
    def eat(self):
        print("Hamster is eating seeds.")

    def sleep(self):
        print("Hamster is sleeping in its nest.")

    def move_to(self):
        print("Hamster scurries to a new hiding spot.")

    def plan_escape(self):
        print("Hamster is planning its escape.")
