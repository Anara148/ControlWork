# задание 1
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age


    def get_age(self):
        return self.__age


    def set_age(self, value):
         if value < 0:
            raise ValueError(" Возраст не может быть отрицательным!")
         self.__age = value

person = Person("Елена", 25)
print(f" Имя: {person.name}, Возраст: {person.get_age()} ")

person.set_age(23)
print(f" Новый возрасть: {person.get_age()}")

try:
    person.set_age(-5)
except ValueError as i:
    print(f" Ошибка при изменении возраста!: {i}")

print(f" Текущий возраст: {person.get_age()}")


# задание 2
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Роки")
cat = Cat("Нокс")
print(f" Собака по имени: {dog.name}, издает звук: {dog.speak()}")
print(f" Кот по имении: {cat.name}, издает звук: {cat.speak()}")


# задание 3
class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

def move(vehicale):
    return vehicale.move()

transport = Vehicle()
car = Car()
bike = Bicycle()
print(move(transport))
print(move(car))
print(move(bike))


# задание 4
from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())
print(round(circle.area()))