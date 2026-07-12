# ============================================================
# Topic   : 07 — Object Oriented Programming in Python
# Author  : Rania Rashid
# Ghazi University DG Khan — BS AI (2025–2029)
# ============================================================


# ─────────────────────────────────────────────
# CONCEPT 1: What is Object Oriented Programming?
# OOP is a programming style that organizes code into objects.
# Objects are created from classes and can store data and behavior.
# ─────────────────────────────────────────────

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Create objects from the class
my_dog = Dog("Buddy", 3)
my_dog.bark()
my_dog.info()


# ─────────────────────────────────────────────
# CONCEPT 2: Attributes and Methods
# Attributes store data, and methods define actions.
# ─────────────────────────────────────────────

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.brand} is driving.")


car1 = Car("Toyota", "red")
car1.drive()


# ─────────────────────────────────────────────
# CONCEPT 3: Using Multiple Objects
# Each object has its own data.
# ─────────────────────────────────────────────

car2 = Car("Honda", "blue")
car2.drive()
print(f"Car 1 brand: {car1.brand}")
print(f"Car 2 brand: {car2.brand}")


# ─────────────────────────────────────────────
# CONCEPT 4: Inheritance
# A child class can inherit features from a parent class.
# ─────────────────────────────────────────────

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says meow")


class Bird(Animal):
    def speak(self):
        print(f"{self.name} says chirp")


cat = Cat("Milo")
bird = Bird("Tweety")

cat.speak()
bird.speak()


# ─────────────────────────────────────────────
# CONCEPT 5: Why OOP Is Useful
# OOP makes programs easier to organize and reuse.
# ─────────────────────────────────────────────

print("\nObject Oriented Programming helps structure code clearly.")
print("It is useful for building larger and more complex programs.")
