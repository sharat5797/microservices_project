from abc import ABC, abstractmethod

class Measures(ABC):
    @abstractmethod
    def getMeasureResponse():
        pass

    @abstractmethod
    def getSource():
        pass