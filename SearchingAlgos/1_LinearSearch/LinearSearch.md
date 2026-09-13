# Linear Search

Linear search is a simple searching technique in which we check each element of an array one by one from the beginning until we find the target value.

## How it works

- Start from the first element
- Compare it with the value you want to find
- If it matches, stop
- If not, move to the next element
- Repeat until the value is found or the list ends

## Example

Array: [8, 3, 12, 5, 9]
Target: 12

We check:

- 8 → not match
- 3 → not match
- 12 → match

So, the search ends successfully at index 2.

## Simple Diagram

```text
Index:    0    1    2    3    4
Array:   [8,  3,  12,  5,  9]
                 ^
                 |
               check here

Search for: 12

Step 1: compare 8  -> not found
Step 2: compare 3  -> not found
Step 3: compare 12 -> found
```

## Pseudocode

```text
linearSearch(arr, target):
    for i from 0 to length(arr) - 1:
        if arr[i] == target:
            return i
    return -1
```

## Time Complexity

- Best case: O(1)
- Average case: O(n)
- Worst case: O(n)

Here, n is the number of elements.

## Space Complexity

- O(1)

## When to use it

- When the list is small
- When the data is unsorted
- When simplicity is more important than speed

## Summary

Linear search is the easiest searching method. It is easy to understand and implement, but it may take more time for large arrays because it checks every element.
