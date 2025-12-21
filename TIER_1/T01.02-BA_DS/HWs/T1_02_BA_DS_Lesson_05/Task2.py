def binary_search(arr, target):
    low, high = 0, len(arr) - 1             # start borders

    iterations = 0                          # zero before start
    upper_bound = arr[-1]

    while low <= high:
        iterations += 1                     # start counter
        mid = (low + high) // 2             # middle index

        if arr[mid] < target:
            low = mid + 1                   # go right
        elif arr[mid] > target:
            upper_bound = arr[mid]
            high = mid - 1                  # go left
        else:
            return (iterations, arr[mid])   # exact match = upper bound

    if upper_bound < target:                # target is bigger than all elements
        upper_bound = None

    return (iterations, upper_bound)


arr = [1.1, 1.2, 5.5, 6.9, 10.0, 10.1, 10.9]  # sorted float array
target = 10.0

result = binary_search(arr, target)
print(result)
