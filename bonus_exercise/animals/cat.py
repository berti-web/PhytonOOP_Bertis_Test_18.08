from .land_animal import LandAnimal


class Cat(LandAnimal):
    def eat(self):
        print("Cat is eating tuna.")

    def sleep(self):
        print("Cat is sleeping on a sunny spot.")

    def move_to(self):
        print("Cat quietly moves to a high perch.")

    def overthrow_humans(self):
        print("Cat plots to overthrow humans.")

    def cough_up_furballs(self):
        print("Cat coughs up a furball.")
