import csv
import timeit
import random


# This is our custom function to find out the maximum value of the given integer list
def myMax(list1):
    # Assume first number in list is largest
    # initially and assign it to variable "max"
    max = list1[0]
    # Now traverse through the list and compare
    # each number with "max" value. Whichever is
    # largest assign that value to "max'.
    for x in list1:
        if x > max:
            max = x

    # after complete traversing the list
    # return the "max" value
    return max


# This function generates a random array of the given size
def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]


# Test different array sizes
array_sizes = list(range(10000, 1000001, 10000))

with open('maxfind_algorithm_times.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['N', 'myMax Function Time (s)', 'Library Function Time (s)'])

    for size in array_sizes:
        arr = generate_random_array(size)

        # testing myMax function
        myMax_time = timeit.timeit(stmt='myMax(arr[:])', globals=globals(), number=1)

        # testing library max function
        libMax_time = timeit.timeit(stmt='max(arr[:])', globals=globals(), number=1)

        writer.writerow([size, myMax_time, libMax_time])