class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<ListNode: {self.data}>'


class SinglyLinkedList():
    def __init__(self):
        self._head = None

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        return f'<SinglyLinkedList: [{values.lstrip(", ")}]>'

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value
        node = ListNode(value)
        # If list is empty just point the header to the new node
        if not self._head:
            self._head = node
        else:
            # if list is not empty, search for the last element and point it to the new node
            current_node = self._head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node

    def pop(self):
        """
        Remove the last element from the list

        Returns: The value of the removed element
        """
        # If list is empty return None
        if not self._head:
            return None
        # If list has only one element, remove it and return its value
        if not self._head.next:
            value = self._head.data
            self._head = None
            return value
        # If list has more than one element, search for the last element and remove it
        current_node = self._head
        while current_node.next.next != None:
            current_node = current_node.next
        value = current_node.next.data
        current_node.next = None
        return value
    


# Test the implementation
def test1():
    list = SinglyLinkedList()
    for i in 'abc':
        list.append(i)

    print(list)
    val = list.pop()
    print("Poped value:", val)
    print(val, list)

def test2():
    list = SinglyLinkedList()
    for i in 'a':
        list.append(i)

    print(list)
    val = list.pop()
    print("Poped value:", val)
    print(val, list)

#test1()
test2()