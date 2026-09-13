from collections import deque


class Queue:
    def __init__(self):
        # deque supports adding to the rear and removing from the front in O(1).
        self.items = deque()
        print(f"Created queue: {list(self.items)} | Time: O(1)")

    def enqueue(self, item):
        # Add an item to the rear of the queue.
        self.items.append(item)
        print(f"Enqueued {item}: {list(self.items)} | Time: O(1)")

    def dequeue(self):
        # Remove and return the item at the front of the queue.
        if not self.items:
            print(f"Cannot dequeue: queue is empty | Queue: {list(self.items)} | Time: O(1)")
            return None

        item = self.items.popleft()
        print(f"Dequeued {item}: {list(self.items)} | Time: O(1)")
        return item

    def peek(self):
        # View the front item without removing it.
        if not self.items:
            print(f"Cannot peek: queue is empty | Queue: {list(self.items)} | Time: O(1)")
            return None

        item = self.items[0]
        print(f"Front item: {item} | Queue: {list(self.items)} | Time: O(1)")
        return item

    def is_empty(self):
        # Check whether the queue contains no items.
        result = len(self.items) == 0
        print(f"Is queue empty? {result} | Queue: {list(self.items)} | Time: O(1)")
        return result

    def size(self):
        # Return the number of items in the queue.
        current_size = len(self.items)
        print(f"Queue size: {current_size} | Queue: {list(self.items)} | Time: O(1)")
        return current_size


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.peek()
    queue.size()
    queue.is_empty()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.is_empty()
