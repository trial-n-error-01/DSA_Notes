# Ternary Search

Ternary Search is a searching algorithm for sorted arrays. It works by dividing the array into three parts instead of two, as in binary search.

## Idea

- The array is split into three sections.
- We compare the target with values at two middle points.
- Based on the comparison, we discard one-third of the array.
- This continues until the target is found or the search range becomes empty.

## Formula

For a sorted array:

mid1 = left + (right - left) // 3
mid2 = right - (right - left) // 3

## Steps

1. Set left = 0 and right = n - 1
2. Compute mid1 and mid2
3. If arr[mid1] == target, return mid1
4. If arr[mid2] == target, return mid2
5. If target < arr[mid1], move right to mid1 - 1
6. Else if target > arr[mid2], move left to mid2 + 1
7. Else search the middle segment: left = mid1 + 1, right = mid2 - 1

## Example

Array:

[1, 3, 5, 7, 9, 11, 13, 15, 17]

Search for 11.

- The array is divided into 3 parts
- We compare 11 with middle values
- The correct section is chosen
- The algorithm keeps narrowing down until 11 is found

## Time Complexity

- Worst case: O(log_3 n)
- Usually slower than binary search in practice

## Space Complexity

- O(1)

## Advantages

- Works well for sorted arrays
- Good divide-and-conquer technique
- Efficient for large search spaces

## Disadvantages

- Less commonly used than binary search
- Usually not faster than binary search

## Summary

Ternary Search divides a sorted array into three parts and removes one part at a time. It is a useful concept in DSA, but binary search is more commonly used because it is simpler and often faster.
