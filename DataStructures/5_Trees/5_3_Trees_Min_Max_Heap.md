## Min-Heaps and Max-Heaps

A **heap** is a complete binary tree commonly stored in an array. It follows a specific ordering rule between each parent and its children.

## Min-Heap

In a min-heap, every parent is less than or equal to its children. The smallest value is always at the root.

```text
		 1
		/ \
	  3   5
	 / \
	8   7
```

## Max-Heap

In a max-heap, every parent is greater than or equal to its children. The largest value is always at the root.

```text
		 9
		/ \
	  7   8
	 / \
	2   5
```

A heap does not fully sort all values. It only guarantees that the minimum or maximum is at the root.

## Heap Complexities

For a heap with `N` elements:

| Operation | Complexity |
| --- | ---: |
| Peek minimum or maximum | O(1) |
| Insert | O(log N) |
| Remove minimum or maximum | O(log N) |
| Build heap from N elements | O(N) |
| Search for an arbitrary value | O(N) |
| Space | O(N) |

Insertion and removal take O(log N) because the element may move through the height of the heap. The height of a complete binary tree is O(log N).

## Common Uses

- Implementing priority queues
- CPU and task scheduling
- Dijkstra's shortest-path algorithm
- A* pathfinding
- Finding the smallest or largest `K` elements
- Tracking a running median with two heaps
- Heap sort
- Event-driven simulations

## Python `heapq` Example

Python provides a min-heap through the `heapq` module:

```python
import heapq

heap = []

heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)

smallest = heapq.heappop(heap)  # 2
```

To simulate a max-heap, store negative values:

```python
max_heap = []

heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -8)

largest = -heapq.heappop(max_heap)  # 8
```
