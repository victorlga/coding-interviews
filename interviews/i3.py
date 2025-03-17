class Stack:

    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def is_empty(self):
        return not self._items
    
    def __len__(self):
        return len(self._items)
    
def sort_stack(stack: Stack) -> None:
    aux_stack = Stack()

    while stack:
        value = stack.pop()

        while not aux_stack.is_empty() and aux_stack.peek() > value:
            aux_value = aux_stack.pop()
            stack.push(aux_value)

        aux_stack.push(value)
    
    while aux_stack:
        aux_value = aux_stack.pop()
        stack.push(aux_value)