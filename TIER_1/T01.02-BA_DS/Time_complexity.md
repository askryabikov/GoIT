# Cheat Sheet: Time Complexity (Algorithms from the module)

**Notation:**  
- `n` — number of elements  
- `m` — pattern length (substring search)  
- `V` — vertices, `E` — edges  
- `W` — capacity (0/1 knapsack)  
- `d` — number of digits/passes (radix), `b` — base/buckets  
- `I` — number of iterations (PageRank)  
- `N` — number of simulations/samples (Monte Carlo)

---

## Sorting Algorithms

| Algorithm | Best | Average | Worst | Notes |
|---|---:|---:|---:|---|
| Bubble sort | `O(n)`* | `O(n^2)` | `O(n^2)` | *Only with early-exit flag (no swaps) |
| Insertion sort | `O(n)` | `O(n^2)` | `O(n^2)` | Fast on nearly sorted data |
| Selection sort | `O(n^2)` | `O(n^2)` | `O(n^2)` | Always quadratic |
| Quick sort | `O(n log n)` | `O(n log n)` | `O(n^2)` | Depends on pivot; usually in-place; unstable |
| Merge sort | `O(n log n)` | `O(n log n)` | `O(n log n)` | Stable; typically needs `O(n)` extra memory |
| Shell sort | depends | typically < `O(n^2)` | often `O(n^2)` | Strongly depends on gap sequence |
| Radix sort | `O(d(n + b))` | `O(d(n + b))` | `O(d(n + b))` | Non-comparison sort |

---

## Search in Arrays / Hash Tables

| Method | Best | Average | Worst | Requirements / Notes |
|---|---:|---:|---:|---|
| Linear search | `O(1)` | `O(n)` | `O(n)` | No assumptions |
| Binary search | `O(1)` | `O(log n)` | `O(log n)` | **Array must be sorted** |
| Indexed-sequential search | — | typically `O(√n)` | `O(n)` | With block size `k≈√n`: `O(log(n/k) + k)` |
| Interpolation search | `O(1)` | `O(log log n)` | `O(n)` | Sorted + near-uniform key distribution |
| Hash table ops (`dict/set`) | `O(1)` | `O(1)` | `O(n)` | Worst case due to collisions (rare) |

---

## Substring Search (Text length `n`, Pattern length `m`)

| Algorithm | Best | Average | Worst | Notes |
|---|---:|---:|---:|---|
| Naive | `O(n)` | `O(nm)` | `O(nm)` | Checks all shifts |
| KMP | `O(n + m)` | `O(n + m)` | `O(n + m)` | Guaranteed linear |
| Rabin–Karp | `O(n + m)` | expected `O(n + m)` | `O(nm)` | Worst with many hash collisions |
| Boyer–Moore | often sublinear | often near `O(n)` | `O(nm)` | Very fast in practice; worst case exists |

---

## Graph Algorithms

| Algorithm | Time | Notes |
|---|---:|---|
| DFS / BFS | `O(V + E)` | Using adjacency lists |
| Dijkstra (binary heap) | `O((V + E) log V)` | Non-negative weights |
| Dijkstra (no heap / matrix) | `O(V^2)` | Simpler; good for dense graphs |
| PageRank (power iteration) | `O(I*(V + E))` | `I` iterations; each pass over edges |

---

## Trees and Heaps

| Structure / Algorithm | Best | Average | Worst | Notes |
|---|---:|---:|---:|---|
| Tree traversal | `O(n)` | `O(n)` | `O(n)` | Pre/In/Post-order |
| BST ops (search/insert/delete) | `O(1)` | `O(log n)` | `O(n)` | Can degenerate into a chain |
| AVL tree ops | `O(log n)` | `O(log n)` | `O(log n)` | Height-balanced guarantee |
| Heapify (build heap) | `O(n)` | `O(n)` | `O(n)` | From array |
| Heap insert / extract | `O(log n)` | `O(log n)` | `O(log n)` | Priority queue |
| Heapsort | `O(n log n)` | `O(n log n)` | `O(n log n)` | Usually unstable |

---

## Greedy / Dynamic Programming / Classic Graph Problems

| Problem / Algorithm | Time | Notes |
|---|---:|---|
| 0/1 Knapsack (DP) | `O(nW)` | Pseudo-polynomial in `W` |
| Fractional Knapsack (greedy) | `O(n log n)` | Sort by value/weight ratio |
| TSP brute force | `O(n!)` | Exact by enumeration |
| TSP Held–Karp (DP) | `O(n^2 * 2^n)` | Exact DP by subsets |
| Floyd–Warshall | `O(V^3)` | All-pairs shortest paths |
| Kruskal (MST) | `O(E log E)` | Sort edges + DSU |
| Prim (MST, heap) | `O(E log V)` | Efficient on sparse graphs |
| Prim (MST, matrix) | `O(V^2)` | Efficient on dense graphs |

---

## Other

| Method | Time | Notes |
|---|---:|---|
| Simplex (Linear Programming) | worst-case exponential | Often fast in practice |
| Randomized algorithms | depends | Usually stated as *expected* complexity |
| Monte Carlo | `O(N)` | `N` simulations/samples |
