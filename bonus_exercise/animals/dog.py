from .land_animal import LandAnimal


class Dog(LandAnimal):
    def eat(self):
        print("Dog is eating kibble.")

    def sleep(self):
        print("Dog is sleeping on the couch.")

    def move_to(self):
        print("Dog runs around the yard.")

    def chase_cars(self):
        print("Dog chases cars.")

    def drool(self):
        print("Dog drools over food.")
