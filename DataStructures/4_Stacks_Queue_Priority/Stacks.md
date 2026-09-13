## Stacks

A stack is a linear data structure that follows **LIFO**:

> Last In, First Out

The last item added to the stack is the first item removed.

```text
Push 10
Push 20
Push 30

Top -> [30]
 [20]
 [10]
```

If we remove an item now, `30` is removed first.

## Common Operations

| Operation | Meaning | Complexity |
| --- | --- | ---: |
| `push` | Add an item to the top | O(1) |
| `pop` | Remove the item from the top | O(1) |
| `peek` or `top` | View the top item without removing it | O(1) |
| `isEmpty` | Check whether the stack is empty | O(1) |
| `size` | Get the number of items | O(1) |

Stack operations are O(1) because they only work with the top item. A stack does not normally allow direct access to items in the middle.

## Implementations

A stack can be implemented using:

- An array
- A dynamic array, such as Java's `ArrayList` or Python's `list`
- A linked list

When using a dynamic array, adding to the top is O(1) amortized. A resize can make one individual `push` O(N), but repeated pushes are O(1) amortized overall.

## Common Uses

- Function call management and recursion
- Undo and redo functionality
- Browser history
- Checking balanced parentheses
- Depth-first search
- Expression evaluation and conversion

For example, parentheses can be checked using a stack:

```text
Input:  ( [ ] )

Read (: push
Read [: push
Read ]: pop [
Read ): pop (

Stack is empty -> balanced
```
