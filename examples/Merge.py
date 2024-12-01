class Node:
    def __init__(self, data):
        self._data = data
        self._next = None
        self._previous = None
    def next(self):
        return self._next
    def previous(self):
        return self._previous
    def link_next(self, node):
        self._next = node
    def link_previous(self, node):
        self._previous = node
    def value(self):
        return self._data


class Sorted_Doubly_Linked_List:
    def __init__(self):
        self._head_node = None

    def print_list(self):
        current = self._head_node
        print('[', end='')
        while current is not None:
            print(current.value(), end='')
            current = current.next()
            if current is not None:
                print(', ', end='')
        print(']')

    def append(self, data):
        new_node = Node(data)

        # Case 1: Empty list
        if self._head_node is None:
            self._head_node = new_node
            return

        # Case 2: Traverse to find the position
        current = self._head_node
        previous = None

        while current is not None and current.value() < data:
            previous = current
            current = current.next()

        # Insert the new node
        if previous is None:
            # Inserting at the head
            new_node.link_next(self._head_node)
            self._head_node.link_previous(new_node)
            self._head_node = new_node
        else:
            # Inserting between `previous` and `current`
            previous.link_next(new_node)
            new_node.link_previous(previous)
            new_node.link_next(current)
            if current is not None:
                current.link_previous(new_node)




    def merge(self, other):
        current = other._head_node
        while current is not None:
            self.append(current.value())
            current = current.next()

        other._head_node = None

        current = self._head_node
        while current is not None:
            other.append(current.value())
            current = current.next()






l1 = Sorted_Doubly_Linked_List()
l1.append(9)
l1.append(5)
l1.append(7)
l1.append(1)
l1.append(3)
l2 = Sorted_Doubly_Linked_List()
l2.append(2)
l2.append(8)
l2.append(0)
l2.append(6)
l2.append(4)
l1.merge(l2)
l1.print_list()
l2.print_list()
assert l1.print_list() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert l2.print_list() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

