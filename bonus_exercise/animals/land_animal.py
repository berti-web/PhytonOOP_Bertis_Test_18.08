from .animal import Animal
from abc import abstractmethod

class LandAnimal(Animal):
    @abstractmethod
    def move_to(self):
        pass
