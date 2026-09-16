# Stack, Queue, and Priority Queue Comparison

Stacks, queues, and priority queues store collections of items, but they differ in the rule used to choose the next item to remove.

| Feature | Stack | Queue | Priority Queue |
| --- | --- | --- | --- |
| Removal rule | LIFO: last in, first out | FIFO: first in, first out | Highest-priority item first |
| Add operation | `push` at the top | `enqueue` at the rear | Insert with a priority |
| Remove operation | `pop` from the top | `dequeue` from the front | Remove highest-priority item |
| View next item | `peek` or `top` | `peek` or `front` | Peek at highest priority |
| Typical implementation | Dynamic array or linked list | `collections.deque` or linked list | Binary min-heap or max-heap |
| Add complexity | O(1) amortized | O(1) with `deque` | O(log N) with a binary heap |
| Remove complexity | O(1) | O(1) with `deque` | O(log N) with a binary heap |
| Peek complexity | O(1) | O(1) | O(1) |
| Search complexity | O(N) | O(N) | O(N) |
| Typical algorithm | DFS | BFS | Dijkstra's or A* |

## Ordering Examples

Suppose these items are added in this order:

```text
A, B, C
```

The removal order depends on the data structure:

```text
Stack:
Add:    A -> B -> C
Remove: C -> B -> A

Queue:
Add:    A -> B -> C
Remove: A -> B -> C

Priority queue:
Add:    A(priority 2), B(priority 5), C(priority 1)
Remove: B -> A -> C
```

## Python Examples

### Stack

Python's `list` is commonly used as a stack because adding and removing at the end are O(1) amortized:

```python
stack = []
stack.append("A")  # push: O(1) amortized
stack.append("B")

item = stack.pop()  # pop: O(1), returns "B"
```

### Queue

Use `collections.deque` for efficient insertion and removal at both ends:

```python
from collections import deque

queue = deque()
queue.append("A")       # enqueue: O(1)
queue.append("B")

item = queue.popleft()   # dequeue: O(1), returns "A"
```

Avoid `list.pop(0)` for queues because shifting the remaining elements costs O(N).

### Priority Queue

Python's `heapq` implements a min-heap, so the smallest value is removed first:

```python
import heapq

priority_queue = []
heapq.heappush(priority_queue, (2, "A"))  # O(log N)
heapq.heappush(priority_queue, (5, "B"))
heapq.heappush(priority_queue, (1, "C"))

priority, item = heapq.heappop(priority_queue)  # O(log N), returns C
```

## When to Use Each One

| Need | Best choice | Reason |
| --- | --- | --- |
| Reverse the order of processing | Stack | The newest item is processed first |
| Process items fairly in arrival order | Queue | The oldest item is processed first |
| Process the most important item first | Priority queue | Priority determines the next item |
| Depth-first traversal | Stack | DFS explores the newest pending node |
| Breadth-first traversal | Queue | BFS explores nodes level by level |
| Shortest path with weighted edges | Priority queue | The next lowest-cost node is selected |

## Main Difference

A **stack** and a **queue** decide the next item using insertion order. A **priority queue** decides using priority instead of insertion order. With equal priorities, a priority queue may use insertion order as a tie-breaker if that behavior is explicitly implemented.
