from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        print("Writing code")

class Designer(Employee):
    def work(self):
        print("Designing UI")
