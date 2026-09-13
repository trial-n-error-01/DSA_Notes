class Stack:
    def __init__(self):
        # Python's list stores the stack items.
        self.items = []
        print(f"Created stack: {self.items} | Time: O(1)")

    def push(self, item):
        # Add an item to the top of the stack.
        self.items.append(item)
        print(f"Pushed {item}: {self.items} | Time: O(1) amortized")

    def pop(self):
        # Remove and return the item from the top of the stack.
        if self.is_empty():
            print(f"Cannot pop: stack is empty | Stack: {self.items} | Time: O(1)")
            return None

        item = self.items.pop()
        print(f"Popped {item}: {self.items} | Time: O(1)")
        return item

    def peek(self):
        # View the top item without removing it.
        if self.is_empty():
            print(f"Cannot peek: stack is empty | Stack: {self.items} | Time: O(1)")
            return None

        item = self.items[-1]
        print(f"Top item: {item} | Stack: {self.items} | Time: O(1)")
        return item

    def is_empty(self):
        # Check whether the stack contains no items.
        result = len(self.items) == 0
        print(f"Is stack empty? {result} | Stack: {self.items} | Time: O(1)")
        return result

    def size(self):
        # Return the number of items in the stack.
        current_size = len(self.items)
        print(f"Stack size: {current_size} | Stack: {self.items} | Time: O(1)")
        return current_size


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.peek()
    stack.size()
    stack.is_empty()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.is_empty()
