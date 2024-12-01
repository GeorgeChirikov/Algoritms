from assigments.chapter_4.PushNPopStack import Stack

class StackBasedQueue():
    def __init__(self):
        self._InboundStack = Stack()
        self._OutboundStack = Stack()
        self._size = 0

    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = [c for c in self._InboundStack]
        values.extend([c for c in self._OutboundStack][::-1])
        return f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(values)}]>'

    def enqueue(self, data):
        self._InboundStack.push(data)
        self._size += 1



    def dequeue(self):
        if self._OutboundStack._size == 0:
            while self._InboundStack._size > 0:
                self._OutboundStack.push(self._InboundStack.pop())
        if self._OutboundStack._size > 0:
            self._size -= 1
            return self._OutboundStack.pop()
        return None

