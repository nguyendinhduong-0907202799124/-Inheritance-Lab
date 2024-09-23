
from reptile import Reptile
class Lizard(Reptile):
    def __init__(self,name):
        super().__init__(name)
        self.name = super().get_name()
