# Exponential Search

Exponential Search is a searching algorithm for sorted arrays. It is useful when the target may be far from the beginning of the array.

## Idea
Instead of checking every element, exponential search first finds a range where the target may exist, and then performs binary search within that range.

## Steps
1. If the first element is the target, return 0.
2. Set index = 1.
3. Keep doubling the index until:
   - the value at that index is greater than the target, or
   - the end of the array is reached.
4. Perform binary search between the last valid index and the current index.

## Example
Array:

[2, 3, 4, 10, 40, 50, 70, 90, 100]

Target = 50

- Start with index 1: 3
- Double: 2, 4, 8
- The target is found between index 4 and 8
- Binary search is then applied to that smaller range

## Time Complexity
- Worst case: O(log n)
- Best case: O(1)

## Space Complexity
- O(1)

## Advantages
- Works efficiently on sorted arrays
- Good when the target is likely far from the start
- Uses binary search after finding the proper range

## Disadvantages
- Only works on sorted arrays
- Usually not better than binary search when the full array is already known

## Summary
Exponential Search finds a range where the target might exist by doubling the index, and then applies binary search in that range. It is a fast method for sorted arrays, especially when the element may be far away.
