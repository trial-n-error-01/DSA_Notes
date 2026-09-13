## Arrays and ArrayLists

An array has a fixed size. An `ArrayList` is a dynamic array whose internal array grows automatically when it becomes full.

### Common Complexities

| Operation | Array | ArrayList |
| --- | ---: | ---: |
| Access by index | O(1) | O(1) |
| Search by value | O(N) | O(N) |
| Add to the end | Not available when full | O(1) amortized |
| Insert at the beginning or middle | O(N) | O(N) |
| Remove from the beginning or middle | O(N) | O(N) |
| Remove from the end | O(1) | O(1) |

Here, `N` is the number of elements in the collection.

### Why Adding to an ArrayList Is Amortized O(1)

Most additions to the end of an `ArrayList` place the new element directly into an unused position, which costs O(1).

When the internal array is full, the `ArrayList` creates a larger array and copies the existing elements into it. That individual resize costs O(N).

However, resizing happens only occasionally. For example, if capacity doubles, the capacities might be:

```text
1 -> 2 -> 4 -> 8 -> 16
```

The total number of copied elements after adding N elements is approximately:

$$1 + 2 + 4 + 8 + \cdots < 2N$$

Therefore, N additions perform O(N) total copying, and the cost per addition is:

$$\frac{O(N)}{N} = O(1)$$

This is called **amortized O(1)**:

- Most individual additions cost O(1).
- A resize can make one addition cost O(N).
- Across a long sequence of additions, the average cost per addition is O(1).

Amortized O(1) does not mean that every operation is guaranteed to take constant time. It describes the total cost distributed across the entire sequence of operations.

The `ArrayList` uses extra memory for unused capacity, so its overall space complexity is O(N).
