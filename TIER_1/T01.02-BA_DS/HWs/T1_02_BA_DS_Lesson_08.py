import heapq

def min_cost(cables):
    heapq.heapify(cables)           # create a minimum heap
    total = 0

    while len(cables) > 1:
        a = heapq.heappop(cables)   # the smallest
        b = heapq.heappop(cables)   # second smallest
        s = a + b                   # cost of this connection

        print(f"Connect {a} + {b} = {s}")  # steps

        total += s
        heapq.heappush(cables, s)   # adds new cable back

    print("Total cost:", total)
    return total


# Example
min_cost([4, 3, 2, 6])
