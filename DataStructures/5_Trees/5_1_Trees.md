## Binary Trees

A binary tree is a tree data structure where each node has at most two children:

- A left child
- A right child

There is no required ordering between node values.

```text
     10
    /  \
   5    20
  / \
 3   7
```

## Types of Binary Trees

### Complete Binary Tree

A complete binary tree has every level completely filled except possibly the last level. The last level is filled from left to right, with no gaps between nodes.

```text
Complete:
     [1]
    /   \
 [2]   [3]
 / \    /
[4][5][6]
```

Complete binary trees are commonly used to implement heaps because their shape can be stored efficiently in an array.

### Full Binary Tree

A full binary tree is a tree where every node has either zero children or exactly two children. No node has only one child.

```text
Full:
   [1]
   / \
 [2] [3]
 / \
[4] [5]
```

Nodes `4`, `5`, and `3` are leaves, while nodes `1` and `2` each have exactly two children.

### Perfect Binary Tree

A perfect binary tree is completely full:

- Every internal node has exactly two children.
- All leaf nodes are at the same level.

```text
Perfect:
    [1]
    / \
 [2]   [3]
 / \   / \
[4][5][6][7]
```

For a perfect binary tree with height `H`:

- Number of nodes: `2^(H + 1) - 1`
- Number of leaves: `2^H`

## Comparison of Binary Tree Types

| Type | Main rule |
| --- | --- |
| Complete | Last level may be incomplete, but nodes fill from left to right |
| Full | Every node has either zero or two children |
| Perfect | Every internal node has two children and all leaves share one level |

Every perfect binary tree is both full and complete. A complete or full binary tree does not have to be perfect.

## Binary Search Trees

A **binary search tree**, or **BST**, is a binary tree with an ordering rule:

- Values in the left subtree are smaller than the node.
- Values in the right subtree are larger than the node.

```text
    10
    /  \
   5    20
   / \     \
  3   7     30
```

This ordering allows a search to eliminate one part of the tree at each step when the tree is balanced.

## Binary Tree Versus Binary Search Tree

| Feature | Binary tree | Binary search tree |
| --- | --- | --- |
| Maximum children | 2 | 2 |
| Value ordering | None required | Left < node < right |
| Searching | Usually O(N) | O(log N) average |
| Searching worst case | O(N) | O(N) if unbalanced |
| In-order traversal | No guaranteed order | Produces sorted values |

## Balanced and Unbalanced BSTs

A balanced BST keeps its height relatively small:

```text
Balanced:
   10
  /  \
  5    20
```

An unbalanced BST can become similar to a linked list:

```text
Unbalanced:
10
 \
  20
   \
   30
```

For a balanced BST:

- Search: O(log N)
- Insert: O(log N)
- Delete: O(log N)

For an unbalanced BST:

- Search: O(N)
- Insert: O(N)
- Delete: O(N)

The key difference is that every BST is a binary tree, but not every binary tree is a BST.
