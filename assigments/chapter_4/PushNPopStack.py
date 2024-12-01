class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def peek(self):
        """
        Returns the value of the top node without altering the stack
        """
        return self._top.data if self._top else None

    def push(self, data):
        """
        Add an element to the stack

        Parameters:
        - 'data': Data/value being added

        Returns: None
        """

        # YOUR CODE HERE. Remove the next line if necessary

        if self._top is None:
            self._top = Node(data)
        else:
            self._top = Node(data, self._top)
        self._size += 1


    def pop(self):
        """
        Remove the top node from the stack and return its content

        Parameters: None

        Returns: The content of the node or None if stack is empty
        """

        # YOUR CODE HERE. Remove the next line if necessary

        if self._top is None:
            return None
        else:
            data = self._top.data
            self._top = self._top.next
            self._size -= 1
            return data


    def __repr__(self):
        # YOUR CODE HERE. Remove the next line if necessary

        current_node = self._top
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<Stack ({self._size} element{plural}): [{values.lstrip(", ")}]>'

# Tests
def test_stack():
    stack = Stack()
    assert len(stack) == 0
    assert stack.peek() is None
    assert str(stack) == '<Stack (0 elements): []>'

    stack.push(1)
    assert len(stack) == 1
    assert stack.peek() == 1
    assert str(stack) == '<Stack (1 element): [1]>'

    stack.push(2)
    assert len(stack) == 2
    assert stack.peek() == 2
    assert str(stack) == '<Stack (2 elements): [2, 1]>'

    assert stack.pop() == 2
    assert len(stack) == 1
    assert stack.peek() == 1
    assert str(stack) == '<Stack (1 element): [1]>'

    assert stack.pop() == 1
    assert len(stack) == 0
    assert stack.peek() is None
    assert str(stack) == '<Stack (0 elements): []>'

    assert stack.pop() is None
    assert len(stack) == 0
    assert stack.peek() is None
    assert str(stack) == '<Stack (0 elements): []>'

    print('All tests passed')

