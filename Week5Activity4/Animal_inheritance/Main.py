from Dog import Dog
from Cat import Cat
from Eagle import Eagle
from Penguin import Penguin
from Salmon import Salmon
from Shark import Shark


def main():
    # Create and demonstrate Dog instance
    dog = Dog("Dog", "Bite")
    print(dog.name)
    print(dog.feature)
    dog.walk()

    # Create and demonstrate Cat instance
    cat = Cat("Cat", "Meow")
    print(cat.name)
    print(cat.feature)
    cat.walk()

    # Create and demonstrate Eagle instance
    eagle = Eagle("Eagle", "Fly")
    print(eagle.name)
    print(eagle.feature)
    eagle.walk()
    eagle.fly()

    # Create and demonstrate Penguin instance
    penguin = Penguin("Penguin", "Swim")
    print(penguin.name)
    print(penguin.feature)
    penguin.walk()
    penguin.swim()

    # Create and demonstrate Salmon instance
    salmon = Salmon("Salmon", "Swim")
    print(salmon.name)
    print(salmon.feature)
    salmon.walk()
    salmon.swim()

    # Create and demonstrate Shark instance
    shark = Shark("Shark", "Bite")
    print(shark.name)
    print(shark.feature)
    shark.walk()

if __name__ == "__main__":
    main()