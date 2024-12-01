# implement node based queue

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'<Node: {self.data}>'

class Queue:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = []
        current = self._tail

        while current:
            if self._size == 0:
                break
            values.append(current.data)
            current = current.prev

        return f'<Queue ({self._size} element{plural}): [{", ".join(values)}]>'

    def enqueue(self, data):
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            current_node = self._tail
            self._tail.next = new_node
            self._tail = new_node
            self._tail.prev = current_node
        self._size += 1

    def dequeue(self):
        if self._head is None:
            return None
        data = self._head.data
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        self._size -= 1
        return data

