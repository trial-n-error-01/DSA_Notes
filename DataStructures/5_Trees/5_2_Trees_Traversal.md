## Tree Traversals

Tree traversal means visiting every node in a tree according to a specific order.

We will use this tree as an example:

```text
   1
   / \
  2   3
  / \
 4   5
```

## In-Order Traversal

In-order traversal visits nodes in this order:

1. Left subtree
2. Current node
3. Right subtree

The pattern is **Left -> Node -> Right**.

For the example tree:

```text
4 -> 2 -> 5 -> 1 -> 3
```

In-order traversal of a binary search tree produces values in sorted order.

## Pre-Order Traversal

Pre-order traversal visits nodes in this order:

1. Current node
2. Left subtree
3. Right subtree

The pattern is **Node -> Left -> Right**.

For the example tree:

```text
1 -> 2 -> 4 -> 5 -> 3
```

Pre-order traversal is useful for copying a tree or serializing its structure.

## Post-Order Traversal

Post-order traversal visits nodes in this order:

1. Left subtree
2. Right subtree
3. Current node

The pattern is **Left -> Right -> Node**.

For the example tree:

```text
4 -> 5 -> 2 -> 3 -> 1
```

Post-order traversal is useful when deleting a tree because children are processed before their parent.

## Complexity

Each traversal visits every node exactly once. If the tree contains `N` nodes:

| Traversal | Time complexity | Auxiliary space |
| --- | ---: | ---: |
| In-order | O(N) | O(H) |
| Pre-order | O(N) | O(H) |
| Post-order | O(N) | O(H) |

`H` is the height of the tree. The O(H) space comes from the recursion call stack or an explicit traversal stack.

- For a balanced tree, `H = O(log N)`, so auxiliary space is O(log N).
- For a completely unbalanced tree, `H = O(N)`, so auxiliary space is O(N).

If the traversal stores the result in a list, that output list requires an additional O(N) space.
