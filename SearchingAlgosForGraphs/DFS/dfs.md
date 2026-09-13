# Depth-First Search (DFS)

Depth-First Search is a graph and tree traversal algorithm. It starts at a node and follows one path as deeply as possible before backtracking to explore another path.

For this tree:

```text
    A
   / \
  B   C
 / \   \
D   E   F
```

One possible DFS traversal from `A` is:

```text
A, B, D, E, C, F
```

The exact order depends on the order in which each node's neighbors are stored.

## How DFS works

1. Start at the source node.
2. Mark the node as visited.
3. Visit an unvisited neighbor.
4. Continue recursively or with a stack until no unvisited neighbor remains.
5. Backtrack and continue with the next available neighbor.

DFS can be implemented in two ways:

- **Recursive DFS:** uses the function call stack.
- **Iterative DFS:** uses an explicit stack, usually `list.append()` and `list.pop()`.

## Complexity

For a graph with `V` vertices and `E` edges:

```text
Time:  O(V + E)
Space: O(V)
```

Each vertex and edge is processed at most once. The space is used by the visited set and the recursion or explicit stack.

### Iterative vs recursive DFS

Both implementations have the same asymptotic complexity:

| Version | Time | Space | Practical note |
| --- | --- | --- | --- |
| Iterative DFS | `O(V + E)` | `O(V)` | Uses an explicit stack |
| Recursive DFS | `O(V + E)` | `O(V)` | Uses the recursion call stack and can hit recursion limits |

For a tree with `N` nodes, both versions take `O(N)` time and `O(N)` space. The choice changes the implementation style, not the overall Big-O complexity.

## DFS compared with BFS

| Feature | DFS | BFS |
| --- | --- | --- |
| Main data structure | Stack or recursion | Queue |
| Traversal order | Deepest path first | Level by level |
| Shortest path in an unweighted graph | Not guaranteed | Guaranteed |
| Memory usage | Often lower on wide graphs | Can be high for wide graphs |
| Best for | Exploring paths and dependencies | Minimum-edge paths and levels |
| Can detect cycles | Yes | Yes |

## Where DFS is used

- Finding connected components
- Detecting cycles in directed and undirected graphs
- Topological sorting of dependency graphs
- Solving mazes and backtracking problems
- Checking whether a path exists
- Finding bridges and articulation points
- Traversing file systems and nested structures
- Exploring game states and decision trees

## When to choose DFS or BFS

Choose **DFS** when:

- You need to explore complete paths.
- The solution is likely to be deep.
- You are solving a backtracking or dependency problem.
- You do not need the shortest path.

Choose **BFS** when:

- You need the shortest path in an unweighted graph.
- You need level-order traversal.
- The answer is likely to be close to the starting node.
- You need the minimum number of moves or edges.

> DFS and BFS have the same asymptotic time complexity, `O(V + E)`. The important difference is their traversal strategy: DFS uses depth and a stack, while BFS uses levels and a queue.
