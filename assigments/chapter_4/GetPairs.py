def get_pairs(number_list=None):
    if number_list is None:
        number_list = []
    even = []
    odd = []
    pairs = []

    for i in range(0, len(number_list)):
        if number_list[i] % 2 == 0:
            even.append(number_list[i])
        else:
            odd.append(number_list[i])

    print(even)
    print(odd)

    for i in range(0, len(even)):
        if i < len(odd) and i < len(even):
            pairs.append((even[i], odd[i]))


    return pairs


def test_get_pairs():
    assert get_pairs([1, 2]) == [(2, 1)]
    assert get_pairs([1, 2, 3, 4]) == [(2, 1), (4, 3)]
    assert get_pairs([1, 2, 3, 4, 5, 6]) == [(2, 1), (4, 3), (6, 5)]
    assert get_pairs([74, 21, 18, 22, 71, 77, 82, 16, 77, 32, 90, 37, 98, 31, 59, 37, 99, 46, 28, 65]) == [(74, 21), (18, 71), (22, 77), (82, 77), (16, 37), (32, 31), (90, 59), (98, 37), (46, 99), (28, 65)]
    assert (get_pairs([93, 55, 9, 36, 83, 98, 77, 97, 26, 81, 72, 48, 18, 20, 2, 88, 82, 51, 58, 30]) == [(36, 93), (98, 55), (26, 9), (72, 83), (48, 77), (18, 97), (20, 81), (2, 51)])

def test_get_pairs2():
    assert get_pairs([93, 55, 9, 36, 83, 98, 77, 97, 26, 81, 72, 48, 18, 20, 2, 88, 82, 51, 58, 30]) == [(36, 93), (98, 55), (26, 9), (72, 83), (48, 77), (18, 97), (20, 81), (2, 51)]

#print(get_pairs([1, 2, 3, 4, 5, 6]))
test_get_pairs2()
print(get_pairs([93, 55, 9, 36, 83, 98, 77, 97, 26, 81, 72, 48, 18, 20, 2, 88, 82, 51, 58, 30]))
