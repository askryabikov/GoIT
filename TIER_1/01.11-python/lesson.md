# Lecture 11 --- Deep English Summary (Serialization: Pickle, JSON, CSV)

## 1. What Serialization Really Is (Deep‑Eng Mindset)

Serialization is the process of **flattening** an in‑memory Python
object into a form that can be stored or transferred.\
Deep‑eng intuition:

> Think of your object as a 3D structure living inside Python's RAM.\
> Serialization compresses it into a 1D stream (bytes or text) so it can
> cross boundaries: disk, network, databases.

Deserialization performs the inverse reconstruction.

Core motivations: - persist state between program runs\
- transmit structured data over networks\
- store configurations, cache heavy computations\
- move complex structures into DBs or files safely

Serialization = reproducibility of object state.

------------------------------------------------------------------------

## 2. Manual Serialization (Before Using Protocols)

Example: writing a dict to a text file.

``` python
expenses = {"hotel": 150, "breakfast": 30}

with open("expenses.txt", "w") as fh:
    for key, value in expenses.items():
        fh.write(f"{key}|{value}
")
```

Deep‑eng note:

> When you invent your own format, you implicitly create a
> **protocol**.\
> That protocol must be consistent, documented, and reversible.

Problems of custom protocols: - separator conflicts\
- type information gets lost\
- manual parsing overhead\
- no interoperability

This is why standardized serialization formats exist.

------------------------------------------------------------------------

## 3. Pickle --- Python's Native Binary Serializer

### 3.1 Concept

Pickle converts Python objects to **byte streams**.\
It is Python‑specific and supports: - dicts, lists, tuples, sets\
- user-defined classes (with restrictions)\
- nested/complex structures

Deep‑eng perspective:

> Pickle walks your object graph, inspects internal state,\
> and builds a symbolic bytecode stream describing *how Python should
> recreate it*.

### 3.2 dumps / loads --- byte‑string control

``` python
import pickle
data = {"key": "value", "num": 42}

serialized = pickle.dumps(data)
obj = pickle.loads(serialized)
```

Use when you need to send data over sockets, pipes, or in‑memory
channels.

### 3.3 dump / load --- file‑level persistence

``` python
with open("data.pickle", "wb") as f:
    pickle.dump(data, f)
```

This produces a binary artifact representing the entire object.

### 3.4 User‑Defined Classes

Pickle stores only **object state**, not class definitions.\
Deep‑eng explanation:

> Pickle expects that the receiving environment already knows\
> what a "Human" class is and how to instantiate it.\
> It serializes the *instance*, not the *blueprint*.

If the class is missing at unpickling time → `AttributeError`.

### 3.5 When to Use Pickle

-   internal application caches\
-   storing Python-specific models\
-   temporary snapshots of computation\
-   IPC (inter‑process communication)

### 3.6 Warnings

Deep‑eng caution:

> Never unpickle data from untrusted sources.\
> Pickle can execute arbitrary code during deserialization.

------------------------------------------------------------------------

## 4. JSON --- Text‑Based, Language‑Agnostic Serialization

JSON is the world's lightweight data exchange standard.

Key features: - readable\
- cross‑language\
- safe by design\
- limited data model

Deep‑eng model:

> JSON reduces Python structures to a "universal minimal subset"
> understood across languages: objects, arrays, strings, numbers,
> booleans.

### 4.1 dumps / loads --- string-level operations

``` python
json_str = json.dumps(data)
restored = json.loads(json_str)
```

Caveats: - tuples → lists\
- numeric keys → strings\
- no support for Python sets or custom classes

### 4.2 dump / load --- working with files

``` python
json.dump(data, f, ensure_ascii=False, indent=4)
```

`ensure_ascii=False` is essential for keeping Cyrillic characters
intact.

Deep‑eng principle:

> JSON is designed for humans *and* machines --- formatting (`indent`)\
> makes it a self-documenting structure.

------------------------------------------------------------------------

## 5. CSV --- Tabular Serialization (Flat and Universal)

CSV is not hierarchical --- it represents rows and columns only.

Deep‑eng intuition:

> CSV is a "2D projection" of your data.\
> Anything tree‑like or nested must be flattened first.

### 5.1 csv.reader --- row-by-row streaming

``` python
with open("data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        ...
```

Use `newline=""` to avoid OS‑specific newline interference.

### 5.2 csv.writer --- streaming structured rows

``` python
writer = csv.writer(f)
writer.writerow([...])
writer.writerows([...])
```

### 5.3 DictReader / DictWriter --- column‑named access

``` python
writer = csv.DictWriter(f, fieldnames=cols)
writer.writeheader()
writer.writerow({"name": "Anna", "age": 22})
```

Deep‑eng value:

> DictReader/Writer turn CSV from a raw byte grid\
> into a semantically meaningful table with named fields.

------------------------------------------------------------------------

## 6. When to Use Which Format (Deep‑Eng Comparison)

  -------------------------------------------------------------------------
  Format       Strengths           Weaknesses           Ideal Use
  ------------ ------------------- -------------------- -------------------
  **Pickle**   full Python         unsafe, Python‑only  caches, internal
               fidelity, complex                        tooling, snapshots
               objects                                  

  **JSON**     portable, readable, limited type system  configs, APIs,
               safe                                     cross‑language data

  **CSV**      simple, universal,  flat only            datasets, exports
               tabular                                  to Excel/BI tools
  -------------------------------------------------------------------------

Deep‑eng takeaway:

> Pickle = maximum fidelity\
> JSON = maximum interoperability\
> CSV = maximum tabular simplicity

------------------------------------------------------------------------

# Final Deep‑Eng Summary

Lecture 11 teaches not "just formats," but the deeper concept:

> **How to turn rich in‑memory structures into portable artifacts**\
> that can survive outside your Python runtime.

You learn to: - serialize arbitrary Python graphs (pickle)\
- exchange structured text with any ecosystem (JSON)\
- integrate with analytics tools and spreadsheets (CSV)

Serialization is a backbone of reproducibility, portability,\
and communication between different layers of a data system.
