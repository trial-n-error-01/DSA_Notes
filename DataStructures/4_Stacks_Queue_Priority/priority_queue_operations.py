import heapq


class PriorityQueue:
    def __init__(self):
        # heapq is a min-heap, so negative priorities create max-priority behavior.
        self.items = []
        self.order = 0
        print(f"Created priority queue: {self.items} | Time: O(1)")

    def enqueue(self, item, priority):
        # The counter preserves FIFO order when two items have the same priority.
        entry = (-priority, self.order, item)
        heapq.heappush(self.items, entry)
        self.order += 1
        print(
            f"Enqueued {item} with priority {priority}: "
            f"{self._display_items()} | Time: O(log N)"
        )

    def dequeue(self):
        # Remove the item with the highest priority.
        if not self.items:
            print(
                f"Cannot dequeue: priority queue is empty | "
                f"Queue: {self._display_items()} | Time: O(1)"
            )
            return None

        negative_priority, _, item = heapq.heappop(self.items)
        priority = -negative_priority
        print(
            f"Dequeued {item} with priority {priority}: "
            f"{self._display_items()} | Time: O(log N)"
        )
        return item

    def peek(self):
        # View the highest-priority item without removing it.
        if not self.items:
            print(
                f"Cannot peek: priority queue is empty | "
                f"Queue: {self._display_items()} | Time: O(1)"
            )
            return None

        negative_priority, _, item = self.items[0]
        priority = -negative_priority
        print(
            f"Highest priority item: {item} with priority {priority}: "
            f"{self._display_items()} | Time: O(1)"
        )
        return item

    def is_empty(self):
        # Check whether the priority queue contains no items.
        result = len(self.items) == 0
        print(
            f"Is priority queue empty? {result} | "
            f"Queue: {self._display_items()} | Time: O(1)"
        )
        return result

    def size(self):
        # Return the number of items in the priority queue.
        current_size = len(self.items)
        print(
            f"Priority queue size: {current_size} | "
            f"Queue: {self._display_items()} | Time: O(1)"
        )
        return current_size

    def _display_items(self):
        # Display entries by priority without changing the heap.
        return [
            (item, -negative_priority)
            for negative_priority, _, item in sorted(self.items)
        ]


if __name__ == "__main__":
    priority_queue = PriorityQueue()
    priority_queue.enqueue("Task A", priority=3)
    priority_queue.enqueue("Task B", priority=1)
    priority_queue.enqueue("Task C", priority=5)
    priority_queue.enqueue("Task D", priority=5)

    priority_queue.peek()
    priority_queue.size()
    priority_queue.dequeue()
    priority_queue.dequeue()
    priority_queue.dequeue()
    priority_queue.dequeue()
    priority_queue.is_empty()
