# Lecture 7 — Deep English Notes  
## Advanced Python Built‑in Modules and Data Structures

This document summarizes the key concepts of Lecture 7, rewritten in **Deep English style**:  
clear, detailed, technically accurate, and easy to understand.

---

# 1. Collections Module Overview  
The `collections` module provides optimized, specialized data structures that go beyond Python’s built‑in list, tuple, set, and dict. They solve common programming tasks with cleaner syntax, better performance, and safer semantics.

---

# 2. Named Tuples (`namedtuple`)  
## What Problem Do They Solve?  
Regular tuples rely on positional indexing: `person[0]`, `person[1]`, etc.  
This quickly becomes unreadable in large data structures.

`namedtuple` creates immutable tuples **with named fields**, allowing attribute access such as `person.name`, improving readability and reducing errors.

### Example  
```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)

print(p.x)   # 10
print(p.y)   # 20
```

### Why It Matters  
- Replaces “magic indexes” with explicit names  
- Immutable → safer data structures  
- Memory‑efficient alternative to classes  

---

# 3. Counter  
`Counter` is a dictionary subclass for counting hashable objects.

### Why It Exists  
Counting manually is error‑prone and repetitive.  
Counter writes the entire counting logic for you.

### Example  
```python
from collections import Counter

marks = [4, 2, 4, 6, 7, 4]
count = Counter(marks)

print(count)  # Counter({4: 3, 2: 1, 6: 1, 7: 1})
```

### Key Feature: `most_common()`  
Returns elements sorted by frequency.

---

# 4. defaultdict  
`defaultdict` automatically initializes missing keys.

### Motivation  
Without defaultdict:  
```python
if key not in d:
    d[key] = []
d[key].append(value)
```

With defaultdict:  
```python
from collections import defaultdict
d = defaultdict(list)
d[key].append(value)
```

### Benefits  
- Eliminates repetitive “if key not in dict” logic  
- Cleaner and safer dictionary operations  

---

# 5. Deque (`collections.deque`)  
A **double‑ended queue** optimized for fast appends/pops on both ends.

### Why Use `deque` Instead of `list`?  
Lists are slow when popping from the beginning (O(n)).  
Deque performs both `append` and `popleft` in O(1).

### Typical Use Cases  
- Task scheduling  
- Sliding windows  
- BFS algorithms  

---

# 6. Decimal — Precise Floating‑Point Arithmetic  
Standard floating‑point (`float`) introduces rounding errors due to binary representation:

```python
print(0.1 + 0.2)  
# 0.30000000000000004
```

`Decimal` solves this by using exact base‑10 representation.

### Example  
```python
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))
```

### Context Precision  
You can control global precision using:

```python
from decimal import getcontext
getcontext().prec = 6
```

Useful in finance, billing, accounting.

---

# 7. Generators and `yield`  
Generators provide **lazy iteration**, meaning values are produced only when requested.

### Why Are Generators Important?
- Save memory (no need to store full list)
- Maintain execution state between yields
- Enable infinite sequences and streaming data processing

### Example  
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
```

### Generator Behavior  
- Execution pauses at each `yield`
- Resumes exactly where it left off
- Raises `StopIteration` when finished  
- Works perfectly with `for` loops

### Real‑World Use Case: Reading Large Files  
```python
def read_lines(path):
    with open(path) as f:
        for line in f:
            yield line.strip()
```

Efficient for processing gigabyte‑size files.

---

# Summary  
Lecture 7 provides tools that improve performance, readability, and scalability:

- **namedtuple** — readable, immutable lightweight records  
- **Counter** — effortless frequency counting  
- **defaultdict** — automatic default values  
- **deque** — high‑performance queue/stack structure  
- **Decimal** — precise arithmetic for money and sensitive data  
- **Generators** — memory‑efficient iterative computations  

These concepts form the foundation for writing **professional, production‑ready Python code**.

