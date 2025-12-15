# Lecture 8 — Functional Programming in Python (Deep English Notes)

## 1. Functions as First-Class Objects
Python treats functions as first-class citizens. This means a function can be:
- assigned to a variable,
- passed as an argument,
- returned from another function,
- stored inside data structures.

This makes functions powerful building blocks for abstraction and composition.

### Example
```python
def greet():
    print("Hello!")

f = greet
f()  # Calling via variable
```

## 2. Passing Functions as Arguments
Higher‑order functions accept other functions as parameters.

```python
from typing import Callable

def apply(a: int, b: int, op: Callable[[int, int], int]) -> int:
    return op(a, b)
```

This pattern supports customizable behavior and reusable logic.

## 3. Returning Functions (Closures)
A closure is created when an inner function *captures* variables from its lexical environment.

```python
def power(exp: int):
    def inner(base: int):
        return base ** exp
    return inner
```

The inner function retains access to `exp` even after `power()` has finished executing.

## 4. Closures & State Retention
Closures can store persistent state without using classes.

```python
def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc
```

## 5. Currying
Currying transforms a function that takes multiple arguments into a chain of functions, each consuming one argument.

```python
def add(a):
    def add_b(b):
        return a + b
    return add_b
```

Useful for pre‑configuring functions and building reusable function variants.

## 6. Decorators
Decorators modify behavior of functions without altering their source code.

```python
def logger(func):
    def inner(*args, **kwargs):
        print("Calling:", func.__name__)
        result = func(*args, **kwargs)
        print("Returned:", result)
        return result
    return inner
```

Applied using the `@decorator` syntax.

### Why decorators matter:
- logging
- access control
- caching
- argument validation
- instrumentation

## 7. List, Set, and Dictionary Comprehensions
Comprehensions provide a readable and expressive way to transform or filter collections.

### List comprehension
```python
squares = [x*x for x in range(10)]
```

### With condition
```python
even = [x for x in numbers if x % 2 == 0]
```

### Dictionary comprehension
```python
sq_map = {x: x*x for x in range(5)}
```

## 8. Lambda Functions
Lambda functions are anonymous one‑line functions.

```python
lambda x: x * 2
```

Commonly used with higher‑order functions.

## 9. Built‑in Functional Tools
### map()
Applies a function to every element of an iterable.

```python
list(map(lambda x: x*x, nums))
```

### filter()
Keeps only elements for which the function returns True.

```python
list(filter(lambda x: x > 0, nums))
```

### any()
Returns True if at least one element is truthy.

### all()
Returns True if *all* elements are truthy.

## 10. Functional Style Summary
Functional programming in Python encourages:
- immutability,
- pure functions,
- predictable transformations,
- composability,
- concise expression through comprehensions and lambdas.

While Python is not purely functional, it offers enough FP tools to create elegant, expressive, and maintainable code.

