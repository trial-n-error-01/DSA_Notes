## Priority Queues

A priority queue is a data structure where each item has a priority. The item with the highest priority is removed first, regardless of when it was added.

```text
Add: (A, priority 3)
Add: (B, priority 1)
Add: (C, priority 5)

Remove first: C
Remove next: A
Remove next: B
```

The priority rule must be defined beforehand. For example, a larger number may mean higher priority, or a smaller number may mean higher priority.

## Common Operations

A priority queue is commonly implemented using a binary heap, such as a min-heap or max-heap.

| Operation | Complexity with binary heap |
| --- | ---: |
| Insert or enqueue | O(log N) |
| Remove highest-priority item | O(log N) |
| Peek at highest-priority item | O(1) |
| Search for an item | O(N) |

When an item is inserted, the heap moves it upward until the heap property is restored. When the highest-priority item is removed, the heap moves another item downward. These movements take O(log N) because a heap has height O(log N).

## Use Cases

- CPU and task scheduling
- Dijkstra's shortest-path algorithm
- A* pathfinding
- Network packet processing
- Emergency-room triage
- Event-driven simulations

## Queue Versus Priority Queue

- A regular queue uses **FIFO**: the oldest item is removed first.
- A priority queue removes the item with the highest priority first.
- If two items have equal priority, FIFO order may be used as a tie-breaker.

```text
Regular queue:
A -> B -> C
Remove: A, then B, then C

Priority queue:
A(priority 2), B(priority 5), C(priority 1)
Remove: B, then A, then C
```

## Priority Queue Implementations

A priority queue is an **abstract data type**, so it describes the behavior that we need rather than one required implementation. Min-heaps and max-heaps are common implementations, but they are not the only choices.

| Implementation | Insert | Peek priority | Remove priority |
| --- | ---: | ---: | ---: |
| Unsorted array or list | O(1) | O(N) | O(N) |
| Sorted array or list | O(N) | O(1) | O(1) |
| Binary min-heap or max-heap | O(log N) | O(1) | O(log N) |
| Balanced binary search tree | O(log N) | O(1) or O(log N) | O(log N) |

Other specialized implementations include Fibonacci heaps, pairing heaps, and bucket-based queues.

## Min-Heaps and Max-Heaps

A **min-heap** removes the smallest priority value first:

```text
1, 3, 5, 8
```

A **max-heap** removes the largest priority value first:

```text
8, 5, 3, 1
```

In Python, `heapq` is a min-heap by default. A max-heap can be simulated by storing negative priorities:

```python
import heapq

heap = []
heapq.heappush(heap, -10)
heapq.heappush(heap, -30)

highest_priority = -heapq.heappop(heap)  # 30
```

The priority queue defines **what behavior is needed**, while the underlying implementation determines the operation complexities.
