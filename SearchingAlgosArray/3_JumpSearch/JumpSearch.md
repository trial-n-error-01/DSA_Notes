# Jump Search

Jump Search is a searching algorithm for sorted arrays. It works by jumping ahead by a fixed step size instead of checking every element one by one.

## Idea

- For a sorted array, we choose a jump size.
- We move forward in blocks of that size.
- When the value at the jump position becomes greater than the target, we go back to the previous position and search linearly within that block.

A common jump size is:

sqrt(n)

where n is the number of elements in the array.

## Example

Suppose the sorted array is:

[ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19 ]

We want to search for 15.

- Jump size = sqrt(10) ≈ 3
- Check positions: 3, 6, 9
- 19 > 15, so we move back to index 6
- Search linearly between 11 and 15
- We find 15 at index 7

## Steps

1. Choose a jump size.
2. Jump through the array in blocks.
3. If the target is smaller than the current jumped value, move backward.
4. Search sequentially inside that block.
5. Return the index if found, otherwise return -1.

## Time Complexity

- Best case: O(1)
- Worst case: O(sqrt(n))
- Average case: O(sqrt(n))

## Space Complexity

- O(1)

## Advantages

- Works efficiently on sorted arrays.
- Simpler than binary search in some cases.
- Requires only constant extra space.

## Disadvantages

- Only works for sorted arrays.
- Slower than binary search for large datasets.

## Jump Search vs Linear Search

- Linear Search: checks every element one by one.
- Jump Search: skips ahead by blocks, reducing comparisons.

## Jump Search vs Binary Search

- Binary Search is usually faster because it divides the array in half each time.
- Jump Search is better than linear search, but not as efficient as binary search.

## Summary

Jump Search is a searching technique for sorted arrays that jumps ahead in blocks and then performs a small linear search in the relevant block. It is a middle-ground between linear search and binary search.
