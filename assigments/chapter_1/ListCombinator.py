def combine_lists(list1, list2):
    new_list = list1 + list2
    # sorting the list
    new_list.sort()
    return new_list


print(combine_lists([1, 3, 5, 7, 9], [0, 2, 4, 6, 8]))
# [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]