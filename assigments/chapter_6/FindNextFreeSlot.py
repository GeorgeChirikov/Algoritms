class HashItem():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'{{{self.key}: {self.value}}}'


class HashTable():
    def __init__(self, size=256):
        self.size = size
        self.slots = [None] * size
        self.used_slots = 0

    def __repr__(self):
        text = ''
        for index, slot in enumerate(self.slots):
            if slot:
                text += f', {index}: {slot}'
        plural = '' if self.used_slots == 1 else 's'
        return f'<HashTable ({self.used_slots} element{plural}): [{text.lstrip(", ")}]'

    def _hash(self, key):
        """
        Hashing function. Can be changed for a custom one.
        """
        return len(key) % self.size

    def _find_free_slot(self, start):
        """
        Starting from 'start' find the next free slot available.

        Parameters:
        - 'start': Starting point for the search.

        Returns: The index of the next free slot or None if no free slots
        """
        for index in range(start, self.size):
            if self.slots[index] is None:
                return index
        for index in range(0, start):
            if self.slots[index] is None:
                return index
        return None

def test_find_free_slot1():
    h = HashTable()

    for c in "abcdefghijklmnopqrstuvwxyz":
        h.slots[(ord(c) * ord(c)) % h.size] = c

    print(h._find_free_slot(0))
    print(h._find_free_slot(1))
    print(h._find_free_slot(10))
    assert h._find_free_slot(0) == 1
    assert h._find_free_slot(1) == 1
    assert h._find_free_slot(10) == 10

def test_find_free_slot2():
    h = HashTable()

    for c in "abcdefghijklmnopqrstuvwxyz":
        h.slots[(ord(c) * ord(c)) % h.size] = c
        h.slots[(ord(c) * ord(c) * ord(c)) % h.size] = c
        h.slots[(ord(c) * ord(c) * ord(c) * ord(c)) % h.size] = c
        h.slots[(ord(c) * ord(c) * ord(c) * ord(c) * ord(c)) % h.size] = c
    h.slots[-1] = h.slots[-2] = 'z'

    print(h._find_free_slot(0))
    print(h._find_free_slot(16))
    print(h._find_free_slot(17))
    print(h._find_free_slot(33))
    print(h._find_free_slot(46))
    print(h._find_free_slot(49))
    print(h._find_free_slot(64))
    print(h._find_free_slot(65))
    print(h._find_free_slot(253))
    print(h._find_free_slot(254))
    print(h._find_free_slot(255))

    assert h._find_free_slot(0) == 1
    assert h._find_free_slot(16) == 18
    assert h._find_free_slot(17) == 18
    assert h._find_free_slot(33) == 34
    assert h._find_free_slot(46) == 46
    assert h._find_free_slot(49) == 50
    assert h._find_free_slot(64) == 66
    assert h._find_free_slot(65) == 66
    assert h._find_free_slot(253) == 253
    assert h._find_free_slot(254) == 1
    assert h._find_free_slot(255) == 1

def test_hash_table():
    h = HashTable()

    h.slots = [True] * 256
    h.slots[0] = None

    print(h._find_free_slot(0))
    print(h._find_free_slot(16))
    print(h._find_free_slot(17))
    print(h._find_free_slot(33))
    print(h._find_free_slot(46))
    print(h._find_free_slot(49))
    print(h._find_free_slot(64))
    print(h._find_free_slot(65))
    print(h._find_free_slot(253))
    print(h._find_free_slot(254))
    print(h._find_free_slot(255))

    assert h._find_free_slot(0) == 0
    assert h._find_free_slot(16) == 0
    assert h._find_free_slot(17) == 0
    assert h._find_free_slot(33) == 0
    assert h._find_free_slot(46) == 0
    assert h._find_free_slot(49) == 0
    assert h._find_free_slot(64) == 0
    assert h._find_free_slot(65) == 0
    assert h._find_free_slot(253) == 0
    assert h._find_free_slot(254) == 0
    assert h._find_free_slot(255) == 0


test_find_free_slot1()
test_find_free_slot2()