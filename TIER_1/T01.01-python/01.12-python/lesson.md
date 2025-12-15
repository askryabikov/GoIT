# Lecture 12 --- Deep English Summary (Controlling Serialization & Copying Objects)

## 1. Deep‑Eng: Why Control Serialization?

Serialization normally "just works", but only if: - every attribute is
serializable - no external resources are attached - state is clean and
self‑contained

Deep‑eng mindset:

> A Python object is not just data --- it may include *open files*,
> *network sockets*, *handles*, *buffers*, *threads*.\
> Pickle cannot freeze such resources, so you must teach your object
> *how to serialize itself*.

This is where `__getstate__` and `__setstate__` come into play.

------------------------------------------------------------------------

## 2. `__getstate__` & `__setstate__` --- Customizing Pickle Behavior

These are *serialization hooks*.

### How pickle uses them internally:

1.  When serializing (`pickle.dump`):
    -   If `__getstate__` exists, pickle calls it.
    -   Its return value becomes the saved state.
2.  When deserializing (`pickle.load`):
    -   If `__setstate__` exists, pickle calls it.
    -   The provided dict is used to reconstruct the object.

Deep‑eng perspective:

> `__getstate__` extracts the "portable essence" of your object.\
> `__setstate__` restores the object to a valid operational state.

Example: Removing non‑serializable attributes.

``` python
def __getstate__(self):
    state = self.__dict__.copy()
    del state["is_active"]
    return state

def __setstate__(self, state):
    self.__dict__.update(state)
    self.is_active = False
```

This pattern is essential for: - open file handles\
- DB connections\
- network sockets\
- caches\
- temporary runtime flags

------------------------------------------------------------------------

## 3. Understanding `__dict__` (the object's internal state)

Every normal Python object has a personal storage dictionary:

``` python
obj.__dict__ == {"attr_name": value, ...}
```

Deep‑eng interpretation:

> `__dict__` is the object's "memory dump".\
> Pickle saves exactly what you place in that memory dump --- no more,
> no less.

Because of this, you can dynamically: - add attributes\
- remove attributes\
- alter structure on the fly

Serialization hooks simply manipulate this dict.

------------------------------------------------------------------------

## 4. Handling Non‑Serializable Attributes (File Example)

A classic example: file descriptors.

``` python
self.fh = open(...)
```

Pickle cannot serialize an open file →
`TypeError: cannot pickle '_io.TextIOWrapper'`.

Solution:

-   strip file handle from saved state
-   reopen it when restoring

Deep‑eng logic:

> Resources cannot be serialized, but *resource configuration* can.

------------------------------------------------------------------------

## 5. Copying Objects --- Deep‑Eng Mental Model

Copying is *not* the same as serializing.

### Fundamental idea:

> Names are not objects; names are references to objects.\
> A "copy" may still point to the same data unless handled carefully.

This leads to:

-   shallow copy --- copies only top-level container
-   deep copy --- recursively clones everything reachable

------------------------------------------------------------------------

## 6. Shallow Copy: `copy.copy()`

Shallow copy: - creates a new container - inserts the *same underlying
objects* inside

``` python
copy_list = copy.copy(my_list)
```

Deep‑eng analogy:

> A shallow copy is like copying a box but leaving the same items
> inside.

For lists/dicts with nested objects → nested items remain shared.

------------------------------------------------------------------------

## 7. Deep Copy: `copy.deepcopy()`

Deep copy: - clones container - recursively clones nested structures

Deep‑eng analogy:

> A deep copy is copying the box *and* duplicating every item inside it.

Uses a `memo` dictionary to avoid: - infinite recursion\
- multiple copies of same object

------------------------------------------------------------------------

## 8. Customizing Copying (`__copy__` and `__deepcopy__`)

User-defined classes can override default copy behavior.

### Why override?

-   avoid copying heavy datasets\
-   create shared references intentionally\
-   clone only safe parts of the object\
-   preserve identity semantics

### Magic methods:

``` python
def __copy__(self):
    return ShallowClone(...)

def __deepcopy__(self, memo):
    return DeepClone(...)
```

Deep‑eng insight:

> Copying is not just duplication --- it is *policy*.\
> You decide which parts of your object are identity and which are data.

------------------------------------------------------------------------

## 9. Complex Object Copying (Nested Objects)

Example: object containing another object.

Shallow copy: - nested objects shared\
Deep copy: - nested objects duplicated

Deep‑eng summary:

> Shallow copy preserves relationship graph.\
> Deep copy reproduces the structure independently.

------------------------------------------------------------------------

## 10. Large-Data Scenario (Why Custom Deepcopy Matters)

If an object stores: - gigabytes of data\
- memory-mapped arrays\
- global caches\
- shared datasets

You do *not* want to deep-copy such resources.

Solution: custom `__deepcopy__`:

``` python
new_prefs = deepcopy(self.preferences)
new = UserSettings(new_prefs, self.large_data_reference)
```

Deep‑eng principle:

> Copy only what is *semantic state*, not what is *heavy payload*.

------------------------------------------------------------------------

# Final Deep‑Eng Summary

Lecture 12 teaches **fine‑grained control over object persistence and
duplication**.

You learn to:

### ✔ Teach objects how to serialize themselves

via `__getstate__` and `__setstate__`.

### ✔ Strip and rebuild non‑serializable attributes

like file handles, sockets, DB connections.

### ✔ Understand the true structure of an object (`__dict__`)

and control exactly what goes into the saved state.

### ✔ Master Python's two copying models

-   shallow copy (structure only)\
-   deep copy (full recursive duplication)

### ✔ Build custom copying logic

to optimize performance, memory use, and correctness.

**Deep‑eng takeaway:**

> Serialization and copying are not "dump my object somewhere".\
> They are *intentional engineering decisions*, defining what identity
> means for your object ---\
> what must be preserved, what must be rebuilt, and what must never be
> duplicated.
