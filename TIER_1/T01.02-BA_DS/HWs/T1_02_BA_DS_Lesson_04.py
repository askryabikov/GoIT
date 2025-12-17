import timeit  # measuring execution time
import random  # random numbers generator


def measure_time(sort_func, data):           # function to measure sorting time
    start_time = timeit.default_timer()      # start timer
    sorted_data = sort_func(data[:])         # sort a copy of data
    execution_time = timeit.default_timer() - start_time     # calculate elapsed time
    return sorted_data, execution_time       # return sorted list and time


def insertion_sort(lst):                     # Sort algorithm: INSERTION
    for i in range(1, len(lst)):             # I: check from second index to the end
        key = lst[i]                         # current element we want to insert
        j = i - 1                            # J: deduct 1 index from I
        while j >= 0 and key < lst[j]:       # CONDITION: shift bigger elements to the right
            lst[j + 1] = lst[j]              # move element one step right
            j -= 1                           # move left
        lst[j + 1] = key                     # put key into correct position
    return lst


def merge_sort(arr):                         # Sort algorithm: MERGING
    if len(arr) <= 1:                        # base case for 0 or 1 digit
        return arr                           

    mid = len(arr) // 2                      # find middle index
    left_half = arr[:mid]                    # take left and right parts
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))  # sort parts and merge


def merge(left, right):                      # merge two sorted lists
    merged = [] 
    left_index = 0                           # default index for each side
    right_index = 0 

    while left_index < len(left) and right_index < len(right):  # compare until no digits left
        if left[left_index] <= right[right_index]:              # if left item is smaller or equal to right side:
            merged.append(left[left_index])                     # then add left item
            left_index += 1                                     # then move left pointer
        else:                                                   # if right side is smaller:
            merged.append(right[right_index])                   # add right item
            right_index += 1                                    # then move right pointer

    while left_index < len(left):                               # add left side when right side is finished
        merged.append(left[left_index])                         # add item
        left_index += 1                                         # move pointer

    while right_index < len(right):                             # then add remaining digits from right side
        merged.append(right[right_index])                       # add item
        right_index += 1                                        # move pointer

    return merged                                               # return merged sorted list


def timsort(data):                # built-in Timsort
    return sorted(data)


data_smallest = [random.randint(0, 1_000) for _ in range(10)]   # generate random numbers: 10, 100, 1000 or 10000
data_small = [random.randint(0, 1_000) for _ in range(100)]
data_big = [random.randint(0, 1_000) for _ in range(1_000)]
data_largest = [random.randint(0, 10_000) for _ in range(10_000)]


test_data = [                     # list of datasets for testing
    data_smallest,
    data_small,
    data_big,
    data_largest,
]

sorting_functions = [             # list of sorting functions to test
    insertion_sort, 
    merge_sort, 
    timsort,
]


for data in test_data:                                          # go through each dataset
    print("\nDATA SIZE:", len(data))                            # show quantity of elements in dataset
    for sort_func in sorting_functions:                         # check each sorting algorithm
        sorted_data, seconds = measure_time(sort_func, data)    # measure time
        print(sort_func.__name__, "time:", seconds)             # print function name and time
