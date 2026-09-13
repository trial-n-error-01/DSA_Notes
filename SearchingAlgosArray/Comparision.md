# Comparison of Searching Algorithms

This comparison covers the search algorithms discussed in this folder: Linear Search, Binary Search, Jump Search, Interpolation Search, Ternary Search, Exponential Search, and Rabin-Karp.

## Quick Comparison Table

| Algorithm | Data Type | Sorted Required | Best Case | Average Case | Worst Case | Space | Main Idea |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Linear Search | Arrays / Lists | No | O(1) | O(n) | O(n) | O(1) | Checks elements one by one |
| Binary Search | Arrays | Yes | O(1) | O(log n) | O(log n) | O(1) iterative / O(log n) recursive | Split search space in half |
| Jump Search | Arrays | Yes | O(1) | O(sqrt(n)) | O(sqrt(n)) | O(1) | Jump in blocks, then search within a block |
| Interpolation Search | Arrays | Yes; uniformly distributed | O(1) | O(log log n) | O(n) | O(1) | Estimate the likely target position |
| Ternary Search | Arrays | Yes | O(1) | O(log_3 n) | O(log_3 n) | O(1) | Split array into three parts |
| Exponential Search | Arrays | Yes | O(1) | O(log n) | O(log n) | O(1) | Find a range, then do binary search |
| Rabin-Karp | Strings / Text | No fixed sorted requirement | O(n + m) | O(n + m) | O(n × m) | O(1) | Compare pattern and text using hashing |

---

## 1. Linear Search

Linear Search is the simplest search method. It scans every element from the beginning until it finds the target or reaches the end.

### Characteristics

- Works on unsorted data
- Easy to understand and implement
- Very slow for large datasets

### Complexity

- Best: O(1)
- Average: O(n)
- Worst: O(n)
- Space: O(1)

### When to use

- Small arrays
- Unsorted lists
- When simplicity matters more than speed

### Summary

Linear search is reliable and straightforward, but it is not efficient for large collections because it checks each item one by one.

---

## 2. Binary Search

Binary Search works only on sorted arrays. It repeatedly divides the search range in half and discards the half where the target cannot be.

### Characteristics

- Very fast for large sorted arrays
- Much better than linear search for large data
- Requires sorted input

### Complexity

- Best: O(1)
- Average: O(log n)
- Worst: O(log n)
- Space: O(1) iterative, O(log n) recursive

### When to use

- Sorted arrays or lists
- Large datasets where speed matters
- Applications needing efficient searching

### Summary

Binary search is the most common and efficient search method for sorted arrays. It is faster than linear search because it removes half the search space at each step.

---

## 3. Jump Search

Jump Search is a compromise between linear search and binary search. It works on sorted arrays by jumping ahead in blocks and then doing a small linear search inside the relevant block.

### Characteristics

- Better than linear search
- Not as fast as binary search
- Uses a fixed block size, usually sqrt(n)

### Complexity

- Best: O(1)
- Average: O(sqrt(n))
- Worst: O(sqrt(n))
- Space: O(1)

### When to use

- Sorted arrays
- Situations where binary search is not preferred or available

### Summary

Jump search reduces the number of comparisons by skipping blocks, but it is still less efficient than binary search for large inputs.

---

## 4. Interpolation Search

Interpolation Search is used for sorted arrays where the values are uniformly distributed. Instead of checking the middle element, it estimates where the target is likely to be based on the value range.

### Characteristics

- Very efficient on evenly distributed data
- More intelligent than simple midpoint splitting
- Can degrade badly on unevenly distributed arrays

### Complexity

- Best: O(1)
- Average: O(log log n) for uniformly distributed data
- Worst: O(n)
- Space: O(1)

### When to use

- Sorted arrays with evenly spaced values
- Large datasets where distribution is predictable

### Summary

Interpolation search can be extremely fast in ideal conditions, but it is not always reliable because its performance depends heavily on data distribution.

---

## 5. Ternary Search

Ternary Search divides the sorted array into three parts instead of two and eliminates one third of the search space each step.

### Characteristics

- Similar to binary search
- Works only on sorted arrays
- Usually less practical than binary search

### Complexity

- Worst: O(log_3 n)
- Space: O(1)

### When to use

- Sorted arrays
- Learning divide-and-conquer search patterns

### Summary

Ternary search is conceptually interesting and efficient in theory, but binary search is usually preferred because it is simpler and often faster in practice.

---

## 6. Exponential Search

Exponential Search is useful when the target may be far from the beginning of a sorted array. It first finds a range where the target might exist and then performs binary search inside that range.

### Characteristics

- Efficient for sorted arrays when target is likely far away
- Combines range-finding and binary search
- Requires sorted array

### Complexity

- Best: O(1)
- Average: O(log n)
- Worst: O(log n)
- Space: O(1)

### When to use

- Sorted arrays
- Searching for an element that may be near the end or far from the start

### Summary

Exponential search is a good choice when the target might be located far away and the array is sorted. It reduces the search to a smaller manageable range before performing binary search.

---

## 7. Rabin-Karp Algorithm

Rabin-Karp is mainly a string-searching algorithm, not a typical array search method. It searches for a pattern in a text by comparing hashes of substrings instead of comparing every character directly.

### Characteristics

- Best for text and pattern matching
- Uses hashing and rolling hash technique
- Good for multiple-pattern matching in some use cases

### Complexity

- Average: O(n + m)
- Worst: O(n × m)
- Space: O(1)

Where:

- n = text length
- m = pattern length

### When to use

- Pattern matching in text
- Large text analysis
- Multiple pattern matching and plagiarism detection

### Summary

Rabin-Karp is highly useful for string matching because hashing allows fast comparisons. However, hash collisions can make its worst-case performance worse than expected.

---

## Average-Case Complexity Graph

The following chart compares the average-case complexity of the algorithms on a log scale. Lower is better.

```text
Average Complexity (log scale)

O(n)        Linear Search            ██████████████████████
O(log n)    Binary Search            ████████████████
            Exponential Search       ████████████████
O(sqrt n)   Jump Search              ██████████
O(log log n) Interpolation Search     ████████
O(log_3 n)  Ternary Search           ████████
O(n + m)    Rabin-Karp               ████████████

Legend:
- Higher bar = more work on average
- Lower bar = more efficient search
```

For a more direct comparison, here is the same idea in terms of growth:

```text
Linear Search        -> O(n)
Binary Search        -> O(log n)
Exponential Search   -> O(log n)
Jump Search          -> O(sqrt n)
Interpolation Search -> O(log log n)  (best-case on uniform data)
Ternary Search       -> O(log_3 n)
Rabin-Karp           -> O(n + m)  (string matching)
```

## Final Comparison

- Linear Search is the easiest but slowest general-purpose option.
- Binary Search is the standard choice for sorted arrays because it is efficient and simple.
- Jump Search is a middle ground between linear and binary search.
- Interpolation Search can be very fast on evenly distributed data, but it is not always reliable.
- Ternary Search is similar to binary search but usually less practical.
- Exponential Search is useful when the target may be far from the beginning.
- Rabin-Karp is not for sorted arrays; it is designed for text pattern matching using hashes.

## Conclusion

Different searching algorithms are useful in different situations. The best choice depends on:

- whether the data is sorted,
- whether the data is numeric or textual,
- how large the dataset is,
- and how the data is distributed.

For sorted numeric arrays, Binary Search is usually the best default choice. For text pattern matching, Rabin-Karp is more relevant. For small or unsorted data, Linear Search remains the simplest and most practical option.
