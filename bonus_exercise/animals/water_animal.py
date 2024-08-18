from .animal import Animal
from abc import abstractmethod

class WaterAnimal(Animal):
    @abstractmethod
    def swim_to(self):
        pass
