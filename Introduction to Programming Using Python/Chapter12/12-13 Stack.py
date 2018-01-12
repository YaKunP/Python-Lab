class Stack:
    def __init__(self):
        self.__elements = []

    # Return True if the stack is empty
    def isEmpty(self):
        return len(self.__elements) == 0

    # Return the element at the top of the stack
    # without removing it from the stack
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements[len(elements) - 1]
    # Store an element at the top of the stack
    def push(self, value):
        self.__elements.append(value)

    # Remove the element at the top of the stack and return it
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements.pop()

    # Return the size of the stack
    def getSize(self):
        return len(self.__elements)