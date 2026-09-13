class ArrayListOperations:
    def __init__(self):
        # Python's list is a dynamic array, similar to Java's ArrayList.
        self.items = []
        print(f"Created list: {self.items}")

    def add(self, item):
        # Add an item to the end of the list.
        self.items.append(item)
        print(f"After adding {item}: {self.items} | Time: O(1) amortized, O(N) during resize")

    def get(self, index):
        # Access an item by its index. Indexing starts at 0.
        item = self.items[index]
        print(f"Element at index {index}: {item} | Time: O(1)")
        return item

    def update(self, index, item):
        # Replace the item at the given index.
        self.items[index] = item
        print(f"After updating index {index}: {self.items} | Time: O(1)")

    def contains(self, item):
        # Check whether an item exists in the list.
        result = item in self.items
        print(f"Contains {item}: {result} | Time: O(N)")
        return result

    def remove(self, index):
        # Remove the item at the given index.
        removed_item = self.items.pop(index)
        print(f"Removed {removed_item}: {self.items} | Time: O(N) for indexed removal")

    def size(self):
        # Return the number of items currently in the list.
        current_size = len(self.items)
        print(f"Current size: {current_size} | Time: O(1)")
        return current_size


if __name__ == "__main__":
    names = ArrayListOperations()
    names.add("Alice")
    names.add("Bob")
    names.add("Charlie")
    names.get(1)
    names.update(1, "Benjamin")
    names.contains("Alice")
    names.remove(0)
    names.size()
