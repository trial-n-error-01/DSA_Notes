## Queues

A queue is a linear data structure that follows **FIFO**:

> First In, First Out

The first item added is the first item removed.

```text
Enqueue 10
Enqueue 20
Enqueue 30

Front -> [10] [20] [30] <- Rear
```

Removing an item returns `10` first.

## Common Operations

| Operation | Meaning | Complexity |
| --- | --- | ---: |
| `enqueue` | Add an item to the rear | O(1) |
| `dequeue` | Remove an item from the front | O(1) with a proper queue |
| `peek` or `front` | View the front item | O(1) |
| `isEmpty` | Check whether the queue is empty | O(1) |

Searching a queue takes O(N), and queues do not normally provide direct random access to the middle.

## Queue Versus Stack

| Feature | Queue | Stack |
| --- | --- | --- |
| Rule | FIFO | LIFO |
| Add item | Rear | Top |
| Remove item | Front | Top |
| Example | Waiting line | Stack of plates |

### Queue Use Cases

- Print-job scheduling
- Customer-service waiting lines
- Task and job processing
- Breadth-first search
- Message and network buffers
- Request handling in servers

### Stack Use Cases

- Function calls and recursion
- Undo and redo
- Browser history
- Depth-first search
- Parentheses matching
- Expression evaluation

## Queue Advantages

- Provides fair processing order
- Useful for scheduling and buffering
- Enqueue and dequeue can both be O(1)
- Prevents newer items from skipping older items

## Queue Disadvantages

- Does not provide direct random access
- Searching takes O(N)
- Items must be processed in order
- A poorly implemented array queue may make `dequeue` O(N) because remaining elements are shifted

## Python Queue Example

Python's `collections.deque` is preferred for queue operations:

```python
from collections import deque

queue = deque()
queue.append("first")   # enqueue: O(1)
queue.append("second")  # enqueue: O(1)

item = queue.popleft()   # dequeue: O(1), returns "first"
```

Using `list.pop(0)` is inefficient because it shifts the remaining elements and costs O(N):

```python
queue = ["first", "second"]
item = queue.pop(0)  # O(N)
```
