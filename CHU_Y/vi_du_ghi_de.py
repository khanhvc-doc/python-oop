from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        #  buộc lớp con phải ghi đè-override
        pass

class Dog(Animal): # thực hiện ghi đè
    def sound(self):
        return "Gâu gâu"

# Ở đây Dog ghi đè phương thức sound()