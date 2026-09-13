## Linked Lists

A linked list is a linear data structure made of **nodes**. Each node stores:

1. A value
2. A reference or pointer to another node

In a singly linked list, each node points to the next node:

```text
[10 | next] -> [20 | next] -> [30 | null]
```

Unlike an array, linked-list elements do not need to be stored next to each other in memory.

## Singly Linked List Complexities

| Operation | Complexity |
| --- | ---: |
| Access by index | O(N) |
| Search by value | O(N) |
| Insert at beginning | O(1) |
| Insert at end | O(N), or O(1) with a tail pointer |
| Insert after a known node | O(1) |
| Remove from beginning | O(1) |
| Remove from end | O(N) |
| Remove after a known node | O(1) |

Access by index is O(N) because the list must be traversed from the head one node at a time. Linked-list insertion and deletion can be O(1) when the relevant node or position is already known because only the links need to be changed.

## Doubly Linked List

A doubly linked list stores references to both the next and previous nodes:

```text
null <- [10] <-> [20] <-> [30] -> null
```

This uses more memory than a singly linked list, but it supports backward traversal and makes some removals easier.

| Operation | Complexity |
| --- | ---: |
| Access by index | O(N) |
| Search by value | O(N) |
| Insert or remove at a known node | O(1) |
| Insert or remove at the beginning | O(1) |
| Insert or remove at the end with a tail pointer | O(1) |

## Arrays Versus Linked Lists

| Feature | Array | Linked list |
| --- | ---: | ---: |
| Access by index | O(1) | O(N) |
| Search by value | O(N) | O(N) |
| Insert or remove at the beginning | O(N) | O(1) |
| Insert or remove in the middle | O(N) | O(1) when the node is known |
| Memory overhead | Lower | Higher because of pointers |

The main tradeoff is:

- **Arrays** provide fast index access but require shifting elements during many insertions and deletions.
- **Linked lists** provide slow index access but support fast insertion and deletion when the location is already known.
