def merge_sort(array):
    """
    Sort the array using the Merge sort algorithm

    Parameters:
    - array: The array to be sorted

    Returns: The sorted array.
    """
    # If array has only 1 element, it is sorted
    if len(array) == 1:
        return array
    # Calculate the midpoint
    midpoint = len(array) // 2
    # And call recursively on the two half arrays.
    first_half = merge_sort(array[:midpoint])
    second_half = merge_sort(array[midpoint:])
    # Merge. Initialize helper variables
    first_index = second_index = 0
    merged_array = []
    # Loop while neither index reaches the end of its half
    while first_index < len(first_half) and second_index < len(second_half):
        # Loop merges the two arrays. Two pointers go forward depending on which one is less than the other
        first_value = first_half[first_index]
        second_value = second_half[second_index]
        # The smaller of the two values get added to the merged list and the pointer of
        # the array it came from advances one position
        if first_value < second_value:
            merged_array.append(first_value)
            first_index += 1
        else:
            merged_array.append(second_value)
            second_index += 1
    # When one of the indices reaches the end of its half, loop ends
    # and the remaining of the other half get added to the merged array.
    # Function has to check which one has to add
    if first_index < len(first_half):
        merged_array.extend(first_half[first_index:])
    elif second_index < len(second_half):
        merged_array.extend(second_half[second_index:])
    # And finally, return the merged array
    return merged_array

# Test the function

def test_merge_sort1():
    array = [6, 8, 5, 1, 2]
    array2 = merge_sort(array)
    print(array2)
    assert array2 == [1, 2, 5, 6, 8]

def test_merge_sort2():
    array = [1, 2, 3, 4, 5]
    array2 = merge_sort(array)
    print(array2)
    assert array2 == [1, 2, 3, 4, 5]

test_merge_sort1()


# def merge_sort(array):
#     """
#     Sort the array using the Merge sort algorithm
#
#     Parameters:
#     - array: The array to be sorted
#
#     Returns: The sorted array.
#     """
#     # If array has only 1 element, it is sorted
#     if len(array) == 1:
#         return array
#     # Calculate the midpoint
#     midpoint = len(array) // 2
#     # And call recursively on the two half arrays.
#     first_half = merge_sort(array[:midpoint])
#     second_half = merge_sort(array[midpoint:])
#     # Merge. Initialize helper variables
#     first_index = second_index = 0
#     merged_array = []
#     # Loop while neither index reaches the end of its half
#     while first_index < len(first_half) and second_index < len(second_half):
#         # Loop merges the two arrays. Two pointers go forward depending on which one is less than the other
#         first_value = first_half[first_index]
#         second_value = second_half[second_index]
#         # The smaller of the two values get added to the merged list and the pointer of
#         # the array it came from advances one position
#         if first_value < second_value:
#             merged_array.append(first_value)
#             first_index += 1
#         else:
#             merged_array.append(second_value)
#             second_index += 1
#     # When one of the indices reaches the end of its half, loop ends
#     # and the remaining of the other half get added to the merged array.
#     # Function has to check which one has to add
#     if first_index < len(first_half):
#         merged_array.extend(first_half[first_index:])
#     elif second_index < len(second_half):
#         merged_array.extend(second_half[second_index:])
#     # And finally, return the merged array
#     return merged_array
