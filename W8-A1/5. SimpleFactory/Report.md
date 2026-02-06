![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-blue?style=for-the-badge)
![Design Pattern](https://img.shields.io/badge/Design%20Pattern-Factory-orange?style=for-the-badge)

# Factory Design Pattern - Code Analysis

## What is the Factory Pattern?

The Factory Design Pattern is a way to create objects without telling the client code which exact class to use. Instead of using `if/else` in the main code, we put the decision logic inside a **factory class**. The factory decides which class to create based on the input it receives.

## How is it implemented in this code?

The main example is in `NamerConsole.py` (and `NameUi.py` for the GUI version). There are four key parts:

**1. Base class — `Namer`**

This is the parent class. It defines two attributes: `first` and `last`.

**2. Two subclasses — `FirstFirst` and `LastFirst`**

- `FirstFirst`: handles names like `"Tom Zhang"` (separated by a space).
- `LastFirst`: handles names like `"Zhang, Tom"` (separated by a comma).

Both classes extend `Namer` and split the name string in different ways.

**3. Factory class — `NamerFactory`**

This is the core of the pattern. The `getNamer()` method checks if the input contains a comma:

```python
class NamerFactory():
    def __init__(self, namestring):
        self.name = namestring

    def getNamer(self):
        if self.name.find(",") > 0:
            return LastFirst(self.name)   # comma found → last name first
        else:
            return FirstFirst(self.name)  # no comma → first name first
```

The factory hides the creation logic. The caller does not need to know which subclass is used.

**4. Client code — `Builder`**

The `Builder` class simply calls the factory and uses the result:

```python
namerFact = NamerFactory(name)
namer = namerFact.getNamer()
print(namer.first, namer.last)
```

It does not care whether the returned object is `FirstFirst` or `LastFirst`.

## Outcome of the Code

- **Console version (`NamerConsole.py`)**: The user types a name in the terminal. The program splits it into first name and last name and prints the result. It works for both `"Tom Zhang"` and `"Zhang, Tom"`.
- **GUI version (`NameUi.py`)**: Same logic but with a Tkinter window. The user enters a name, clicks "Compute", and the first/last names appear in separate fields.
- **`Cocoon.py`**: Another small factory example. The `Cocoon` class returns either `TrigButterfly` or `AddButterfly` depending on whether the input value is zero or not.

## Why use the Factory Pattern?

The main benefit is that the client code stays simple and does not need to change when new name formats are added. We only need to update the factory class. This makes the code easier to maintain and extend.
