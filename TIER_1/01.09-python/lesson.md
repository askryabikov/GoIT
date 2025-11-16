# Lecture 9 — Deep English Summary  
(Full OOP Foundations, Inheritance, Encapsulation, Polymorphism, Composition, Aggregation, Enums, Dataclasses)

## 1. Introduction to OOP in Python  
Object-Oriented Programming (OOP) is a programming paradigm where software is structured as a collection of interacting objects. Each object combines data (attributes) and behavior (methods). Python is inherently object‑oriented — almost everything is an object.

A **class** acts as a blueprint, while **objects (instances)** are individual realizations of that blueprint.

---

## 2. Classes and Objects  
```python
class Person:
    pass

p = Person()
```
A class defines structure and behavior, while an object is a concrete instance created from it.

Naming convention: Class names use **CamelCase**.

---

## 3. Class Attributes vs Instance Attributes  
- **Class Attributes** — shared across all instances.  
- **Instance Attributes (fields)** — unique to each object.

```python
class User:
    default_role = "guest"  # class attribute

    def __init__(self, name):
        self.name = name    # instance attribute
```

---

## 4. Methods and `self`  
Every instance method receives the instance as its first argument (`self`).  
Python automatically provides `self` when calling methods.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(f"My name is {self.name}")
```

---

## 5. Encapsulation  
Encapsulation hides internal implementation and exposes only a controlled interface.

Python has three visibility levels (by convention):
- **public** — no underscore  
- **protected** — `_name`  
- **private** — `__name` (name‑mangling)

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self._is_active = True      # protected
        self.__secret = "hidden"    # private
```

Private attributes are name-mangled and accessible as:
```python
obj._ClassName__secret
```

---

## 6. Inheritance  
A class can extend another class, inheriting attributes and methods.

```python
class Animal:
    def make_sound(self): pass

class Cat(Animal):
    def make_sound(self): return "Meow"
```

Use `super()` to call the parent constructor:

```python
class Dog(Animal):
    def __init__(self, nickname, age, breed):
        super().__init__(nickname, age)
        self.breed = breed
```

---

## 7. Method Resolution Order (MRO)  
Python resolves methods using a linear ordering defined by the **C3 linearization algorithm**.  
Check the MRO via:

```python
print(ClassName.mro())
```

This is crucial for multiple inheritance.

---

## 8. Polymorphism & Duck Typing  
Polymorphism: Same interface, different behavior.

```python
for animal in animals:
    animal.make_sound()
```

Duck Typing:  
“If it walks like a duck and quacks like a duck — it’s a duck.”

Objects are compatible if they provide the required method.

---

## 9. UserDict, UserList, UserString  
These wrappers (from `collections`) allow safe extension of built‑in container types.

Example:
```python
from collections import UserDict

class Customer(UserDict):
    def phone_info(self):
        return f"{self['name']}: {self['phone']}"
```

---

## 10. Dataclasses  
A modern way to define data‑holder classes without boilerplate.

```python
from dataclasses import dataclass

@dataclass
class Rectangle:
    width: int
    height: int

    def area(self):
        return self.width * self.height
```

Automatically generates:
- `__init__`
- `__repr__`
- `__eq__`  
and more.

---

## 11. Enums  
Enumeration types define a restricted set of constant values.

```python
from enum import Enum, auto

class Status(Enum):
    NEW = auto()
    DONE = auto()
```

---

## 12. Composition vs Aggregation  
Both describe “has-a” relationships.

### **Aggregation**  
Weak ownership.  
Parts can exist independently.

```python
class Owner: ...
class Cat:
    def __init__(self, owner: Owner):
        self.owner = owner
```

### **Composition**  
Strong ownership.  
Parts cannot live without the whole.

```python
class Project:
    def __init__(self):
        self.tasks = []   # Project owns tasks fully
```

---

## 13. Custom Exceptions  
Define domain-specific error types.

```python
class NameTooShortError(Exception): pass
class NameStartsFromLowError(Exception): pass
```

Raising them:

```python
if len(name) < 3:
    raise NameTooShortError("Name too short")
```

---

## Conclusion  
Lecture 9 introduces the foundations of OOP in Python: classes, instances, encapsulation, inheritance, MRO, polymorphism, dataclasses, enums, and sophisticated relationships like composition vs aggregation. These principles form the backbone of modern Python application architecture.

