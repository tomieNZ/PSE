"""
This file is used to demonstrate the inheritance in Python.
I will design a class hierarchy of animals, with the following classes:
- Animal
- Dog
- Corgi
- Cat

The Animal class will be the parent class, and the other classes will inherit from it.
The Dog class will have a method to bite, and the Corgi class will inherit from the Dog class and override the speak method.
The Cat class will inherit from the Animal class and override the speak method.

@author: Yaohui Zhang (tomie)
Date: 2025-12-21
"""
# Parent class
class Animal:
    # initialize the class with name
    def __init__(self, name):
        # print the name of the animal
        print(f"Animal {name} is created!")
        # set the name of the animal
        self.name = name

    # method to speak
    def speak(self):
        # return the sound of the animal
        return f"{self.name} says Animal sound!"

# Dog will inherit the Animal class and override the speak method
class Dog(Animal):
    # method to bite, only dog can bite
    def bite(self):
        return f"{self.name} bites!"
    # override the speak method
    def speak(self):
        return f"{self.name} says Woof!"

# Corgi will inherit the Dog class and override the speak method
class Corgi(Dog):
    # initialize the class with name
    def __init__(self, name):
        # call the parent class constructor
        # super() is used to call the parent class constructor
        # Because the Dog class did not have a constructor, we need to call the parent class constructor
        super().__init__(name)
    # override the speak method
    def speak(self):
        return f"{self.name} says Woof! Woof! I am a Corgi!"
    # method to have short legs, only corgi can have short legs
    def short_legs(self):
        return f"{self.name} has short legs!"


# Cat will inherit the Animal class and override the speak method
class Cat(Animal):
    # override the speak method
    def speak(self):
        return f"{self.name} says Meow!"


def main():
    # create a dog instance
    dog = Dog("Buddy")
    # print the bite and speak method of the dog
    print(dog.bite())
    # print the speak method of the dog
    print(dog.speak())

    # create a corgi instance
    corgi = Corgi("Charlie")
    # print the bite and speak method of the corgi
    print(corgi.bite())
    # print the speak method of the corgi
    print(corgi.speak())
    # print the short legs method of the corgi
    print(corgi.short_legs())
    # create a cat instance
    cat = Cat("Whiskers")
    # print the speak method of the cat
    print(cat.speak())
    # create an animal instance
    animal = Animal("Animal")
    # print the speak method of the animal
    print(animal.speak())



if __name__ == "__main__":
    main()