# Animal Inheritance Demonstration

This folder shows how to use class inheritance in Python. The code uses animals as examples. Animal.py has the main Animal class and three smaller classes called Mammal, Bird, and Fish. These three classes get things from the Animal class. Dog.py and Cat.py are mammal classes. Eagle.py and Penguin.py are bird classes. Salmon.py and Shark.py are fish classes. Main.py shows how to make different animals and use their methods.

Can we see different objects respond differently to the same method call? Yes, we can. Each object has its own name. When we call the same method like walk(), fly(), or swim(), each object uses its own name. For example, dog.walk() prints "Dog is walking." But cat.walk() prints "Cat is walking." All objects use the same method from the Animal class, but they show different results because each object has different information.

Inheritance is useful because it helps us use code again. We write the same behavior once in the Animal class and all other classes can use it. It also helps us organize our code in a clear way. All animals use the same methods but they can have different features. We can also add new animal types easily by using inheritance.
