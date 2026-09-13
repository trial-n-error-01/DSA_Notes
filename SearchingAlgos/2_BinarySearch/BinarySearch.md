# Binary Search

Binary search is a searching algorithm used for finding a value in a sorted array.
It works by repeatedly dividing the search space in half.

## How it works

- Find the middle element of the array
- Compare it with the target value
- If the target is smaller, search the left half
- If the target is larger, search the right half
- Repeat until the value is found or the search space becomes empty

## Example

Array: [2, 5, 8, 12, 16, 23, 38, 45, 57]
Target: 23

```text
[2, 5, 8, 12, 16, 23, 38, 45, 57]
             ^
             middle = 16

23 > 16, so search right half

[23, 38, 45, 57]
   ^
   middle = 38

23 < 38, so search left half

[23]
 ^
 found
```

## Advantages

- Very fast for large sorted arrays
- Much more efficient than linear search
- Reduces the search space by half each step

## Disadvantages

- Works only on sorted data
- If the data is not sorted, it cannot be used directly
- More complex than linear search
- Not necessary for very small arrays

## Time Complexity

For an array of size n:

- Best case: O(1)
- Average case: O(log n)
- Worst case: O(log n)

This is because each step cuts the number of remaining elements in half.

## Space Complexity

- Iterative version: O(1)
- Recursive version: O(log n) due to recursive call stack

## Python Implementation (Iterative)

```python
def binary_search_iterative(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage
numbers = [2, 5, 8, 12, 16, 23, 38, 45, 57]
result = binary_search_iterative(numbers, 23)
print(result)  # Output: 5
```

## Python Implementation (Recursive)

```python
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Example usage
numbers = [2, 5, 8, 12, 16, 23, 38, 45, 57]
result = binary_search_recursive(numbers, 23, 0, len(numbers) - 1)
print(result)  # Output: 5
```

## Summary

Binary search is efficient and fast for sorted data, but it is not useful for unsorted arrays. Compared to linear search, it is much faster for large datasets.
