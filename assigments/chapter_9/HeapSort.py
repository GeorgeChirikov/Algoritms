def heap_sort(array):
    """
    Sort the array using the Heapsort algorithm

    Parameters:
    - array: The array to be sorted

    Returns: Nothing. The array is sorted in-place.
    """
    length = len(array)
    for i in range(length // 2 - 1, -1, -1):
        sift_down(array, i, length - 1)
    for i in range(length - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        sift_down(array, 0, i - 1)
