# Lecture 10 --- Deep English Summary (Magic Methods, Iterators, Context Managers)

## 1. Magic Methods: Controlling Object Behavior Behind the Scenes

Magic methods (also called *dunder methods*) are Python's internal hooks
that define how your objects behave with operators, built‑ins, and
language constructs.\
Names always start and end with `__`, e.g., `__init__`, `__str__`,
`__add__`.

### Key idea (deep‑eng):

Inside every operator like `a + b`, Python secretly expands the
expression into a method call:

``` python
a.__add__(b)
```

This means: - You can override how your object *adds*, *subtracts*,
*compares*, *iterates*, *prints*, etc. - Python gives full low‑level
control over object behavior.

### Common categories:

-   **Construction & representation:** `__init__`, `__str__`, `__repr__`
-   **Container emulation:** `__getitem__`, `__setitem__`,
    `__contains__`, `__iter__`
-   **Math operations:** `__add__`, `__sub__`, `__mul__`, etc.
-   **Comparison:** `__eq__`, `__lt__`, `__ge__`
-   **Function‑like behavior:** `__call__`

------------------------------------------------------------------------

## 2. `__init__`, `__str__`, `__repr__` --- Object Lifecycle & Representation

### `__init__`

Executed after Python creates the raw object.\
Used to configure internal state.

Deep‑eng idea: \> Think of `__init__` as the "post‑birth setup". The
object already exists; now you give it a personality.

### `__str__`

Human‑friendly string ("nice print for users").\
Triggered by `print(obj)` or `str(obj)`.

### `__repr__`

Developer‑oriented representation.\
Goal: *Return a string that can ideally recreate the object.*

Deep‑eng rule: \> If `__str__` is for the "customer", `__repr__` is for
the "mechanic".

------------------------------------------------------------------------

## 3. Emulating Containers: `__getitem__`, `__setitem__`, `__contains__`, `__iter__`

Python allows custom classes to mimic lists/dicts.

### `__getitem__(key)`

Defines how `obj[key]` behaves.

### `__setitem__(key, value)`

Defines how assignment works: `obj[key] = value`.

### `__contains__(item)`

Controls `item in obj`.

Deep‑eng explanation: \> When you write `if x in obj`, Python actually
queries the object:\
\> "Hey, do YOU consider x to be inside you?" --- via `__contains__`.

### `__iter__`

Allows looping:

``` python
for element in obj:
```

Deep‑eng: \> An iterator is a "one‑way conveyor belt" --- once moved
forward, you cannot go backward.

------------------------------------------------------------------------

## 4. Operator Overloading (Math)

Any mathematical operator can be redefined.

Useful for: - Vectors\
- Matrices\
- Custom containers\
- Scientific objects\
- Domain‑specific models

Deep‑eng idea: \> Operator overloading lets objects speak the language
of the domain.\
\> A Vector can "understand" `+` the same way humans do.

Example dunders:

``` python
__add__, __sub__, __mul__, __truediv__, __floordiv__, __pow__
```

------------------------------------------------------------------------

## 5. Comparator Methods

Used when comparing objects: - `__eq__` → `==` - `__ne__` → `!=` -
`__lt__` → `<` - `__gt__` → `>` - `__le__` → `<=` - `__ge__` → `>=`

Deep‑eng philosophy: \> Comparison between complex objects must have a
*criterion*\
\> (area, weight, coordinates, priority, etc.).

------------------------------------------------------------------------

## 6. `@property` --- Controlled Access to Attributes

Allows Pythonic getters/setters:

``` python
obj.age = 10    # triggers setter
obj.age         # triggers getter
```

Deep‑eng: \> `@property` gives you "function behavior with attribute
syntax," \> letting your class look simple externally but remain strict
internally.

Use cases: - Validation\
- Encapsulation\
- Lazy computation\
- Read‑only fields

------------------------------------------------------------------------

## 7. Callables (`__call__`) --- Objects Acting Like Functions

If a class has `__call__`, its instances become "function‑like":

``` python
obj = MyFunctor()
obj(10)  # works like a function call
```

Deep‑eng: \> A callable object is a function with memory --- it
preserves state across calls.

Useful for: - Parametrized functions\
- State‑based computation\
- Encapsulated logic\
- Closures implemented in OO style

------------------------------------------------------------------------

## 8. Iterators & Generators

### Full iterator protocol:

-   `__iter__()` → returns iterator\
-   `__next__()` → returns next element or raises `StopIteration`

Deep‑eng: \> Iterator = object that remembers "where it left off."

### Generators using `yield`

A generator is a "lazy mini‑machine" that pauses and resumes execution.

Benefits: - Memory‑efficient\
- Simple syntax\
- Clean state handling

Advanced: - `.send(value)` → send data *into* generator - `.close()` →
stop generator manually

------------------------------------------------------------------------

## 9. Context Managers (`with` statement)

Context managers manage resources safely and automatically.

### Implemented via:

-   `__enter__` --- executed when entering `with`
-   `__exit__` --- executed when exiting

Deep‑eng: \> Context managers guarantee cleanup **no matter what** ---\
\> even if your code fails halfway.

Classic pattern: - Open/close files\
- Acquire/release locks\
- Start/end timers\
- Connect/disconnect resources

### Using `contextlib.contextmanager`

Cleaner, generator‑based syntax for simple context managers.

``` python
@contextmanager
def cm():
    setup
    yield resource
    teardown
```

------------------------------------------------------------------------

# Summary (Deep‑Eng Final Thesis)

Lecture 10 teaches you how to **bend Python to your will** by
controlling how objects behave under: - printing\
- iteration\
- math operations\
- attribute access\
- comparison\
- function calls\
- context management

The core message: \> Python lets you design objects that act, feel, and
interact like built‑in types ---\
\> turning your own abstractions into first‑class citizens of the
language.
