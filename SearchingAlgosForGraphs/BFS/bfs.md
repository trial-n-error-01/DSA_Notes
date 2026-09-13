# BFS (Breadth-First Search)

BFS is a graph/tree traversal algorithm that explores nodes level by level.

## What BFS does

- Start from a chosen node (source/root).
- Visit all neighbors of that node first.
- Then move to the next level of neighbors.
- Use a queue to keep track of which nodes to visit next.

This is why it is called "breadth-first" — it explores the current level before moving deeper.

## Example

If the graph looks like this:

```text
    A
   / \
  B   C
 / \   \
D   E   F
```

A BFS traversal from `A` would visit nodes in this order:

```text
A, B, C, D, E, F
```

## How BFS works

1. Add the starting node to a queue.
2. Mark it as visited.
3. While the queue is not empty:
   - Remove the front node.
   - Visit it.
   - Add all unvisited neighbors to the queue.

## Pseudocode

```python
from collections import deque

def bfs(start):
    visited = set()
    q = deque([start])
    visited.add(start)

    while q:
        node = q.popleft()
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
```

## Use cases

- Finding the shortest path in an unweighted graph
- Level-order traversal in trees
- Checking whether a graph is connected
- Social network traversal
- Web crawling

> Important: BFS guarantees the shortest path only when the graph is unweighted. If edges have different weights, BFS is not the correct algorithm for shortest path; Dijkstra's algorithm is used instead.

## Complexity

For a graph with `V` vertices and `E` edges:

- Time complexity: `O(V + E)`
- Space complexity: `O(V)`

This happens because every vertex is visited once and every edge is checked once.

## Iterative vs recursive BFS

BFS is most commonly implemented iteratively using a queue.

### Iterative BFS

This is the standard and recommended version.

- Uses a queue
- Time complexity: `O(V + E)`
- Space complexity: `O(V)`
- Best for graph traversal and shortest-path problems in unweighted graphs

### Recursive BFS

A recursive version is possible in some custom forms, but it is not the usual way to implement BFS.

- It usually still does total work of `O(V + E)`
- It may also use recursion stack space of `O(V)`
- It is less natural because BFS is fundamentally queue-based
- It can hit recursion depth limits for large graphs

So, in practice, the complexity is usually the same, but iterative BFS is preferred because it matches the algorithm's structure and avoids recursion issues.

### Complexity comparison

For both implementations, where `V` is the number of vertices and `E` is the number of edges:

| Version | Time | Space | Practical note |
| --- | --- | --- | --- |
| Iterative BFS | `O(V + E)` | `O(V)` | Uses an explicit queue and avoids recursion limits |
| Recursive BFS | `O(V + E)` | `O(V)` | Uses a queue plus the recursion call stack |

For a tree with `N` nodes, both versions take `O(N)` time and `O(N)` space. The recursive version can hit Python's recursion-depth limit on a deep graph, so iterative BFS is usually preferred in production code.

## Key takeaway

BFS explores nodes level by level and is especially useful when you need the shortest path in an unweighted graph.

If the graph is weighted, BFS does not account for edge weights, so it cannot be used to guarantee the minimum-cost path.

The standard BFS implementation is iterative, using a queue, and its complexity is:

```text
Time:  O(V + E)
Space: O(V)
```

## Python examples with step-by-step logging

Below is a simple tree structure used by both examples:

```python
# Tree structure
#       A
#      / \
#     B   C
#    / \   \
#   D   E   F

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
```

### 1) Iterative BFS class

```python
from collections import deque

class IterativeBFS:
    def __init__(self, graph):
        self.graph = graph

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        traversal_order = []

        print(f"Starting BFS from: {start}")

        while queue:
            current = queue.popleft()
            traversal_order.append(current)
            print(f"\nCurrent node: {current}")

            neighbors = self.graph.get(current, [])
            print(f"Nodes being considered from {current}: {neighbors}")

            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    print(f"Queued {neighbor} for later processing")

        print(f"\nTraversal order: {traversal_order}")
        return traversal_order


bfs_iter = IterativeBFS(tree)
bfs_iter.bfs('A')
```

Example output:

```text
Starting BFS from: A

Current node: A
Nodes being considered from A: ['B', 'C']
Queued B for later processing
Queued C for later processing

Current node: B
Nodes being considered from B: ['D', 'E']
Queued D for later processing
Queued E for later processing

Current node: C
Nodes being considered from C: ['F']
Queued F for later processing

Current node: D
Nodes being considered from D: []

Current node: E
Nodes being considered from E: []

Current node: F
Nodes being considered from F: []

Traversal order: ['A', 'B', 'C', 'D', 'E', 'F']
```

### 2) Recursive BFS class

```python
class RecursiveBFS:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.order = []

    def bfs_recursive(self, queue):
        if not queue:
            return

        current = queue.pop(0)
        self.order.append(current)
        print(f"\nCurrent node: {current}")

        neighbors = self.graph.get(current, [])
        print(f"Nodes being considered from {current}: {neighbors}")

        for neighbor in neighbors:
            if neighbor not in self.visited:
                self.visited.add(neighbor)
                queue.append(neighbor)
                print(f"Queued {neighbor} for later processing")

        self.bfs_recursive(queue)

    def traverse(self, start):
        self.visited = {start}
        print(f"Starting BFS from: {start}")
        self.bfs_recursive([start])
        print(f"\nTraversal order: {self.order}")
        return self.order


bfs_rec = RecursiveBFS(tree)
bfs_rec.traverse('A')
```

Example output:

```text
Starting BFS from: A

Current node: A
Nodes being considered from A: ['B', 'C']
Queued B for later processing
Queued C for later processing

Current node: B
Nodes being considered from B: ['D', 'E']
Queued D for later processing
Queued E for later processing

Current node: C
Nodes being considered from C: ['F']
Queued F for later processing

Current node: D
Nodes being considered from D: []

Current node: E
Nodes being considered from E: []

Current node: F
Nodes being considered from F: []

Traversal order: ['A', 'B', 'C', 'D', 'E', 'F']
```

### Key difference

- The iterative version uses a queue and is the standard BFS approach.
- The recursive version is less common because BFS is naturally queue-based.
- In both versions, the important part is logging which neighbors are being checked at each step, so you can see the exact part of the tree/graph currently being explored.

### Note

This is a tree example for clarity. In a real graph, the same idea works, but you must track visited nodes to avoid infinite loops from cycles.
