def sift_down(array, start, end):
    """
    This function sinks (if necessary) the given node of a MaxHeap structure

    Parameters:
    - array: The heap array
    - start: The index of the node that should be sinked.
    - end: The end of the heap inside the array. The index of the last node

    Returns: None
    """
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        swap = root
        if array[swap] < array[child]:
            swap = child
        if child + 1 <= end and array[swap] < array[child + 1]:
            swap = child + 1
        if swap == root:
            return
        else:
            array[root], array[swap] = array[swap], array[root]
            root = swap


