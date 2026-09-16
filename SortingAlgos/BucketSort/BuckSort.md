# Bucket Sort

Bucket Sort is a sorting algorithm that distributes values into several groups called **buckets**. Each bucket is sorted separately, and the sorted buckets are joined to produce the final sorted array.

It works especially well when values are distributed fairly evenly across a known range, such as decimal values between `0` and `1`.

## How it works

1. Create a collection of empty buckets.
2. Place each value into its appropriate bucket.
3. Sort each bucket independently.
4. Concatenate the buckets in order.

## Example

Input:

```text
[0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
```

After distributing values into buckets:

```text
Bucket 0: [0.23, 0.25, 0.32]
Bucket 1: [0.42, 0.47]
Bucket 2: [0.51, 0.52]
```

After sorting and combining the buckets:

```text
[0.23, 0.25, 0.32, 0.42, 0.47, 0.51, 0.52]
```

## Complexity

Let `n` be the number of values and `k` be the number of buckets:

| Case | Time complexity |
| --- | --- |
| Average case | `O(n + k)` when values are evenly distributed |
| Best case | `O(n + k)` |
| Worst case | `O(n^2)` when most values fall into one bucket |

Space complexity is usually `O(n + k)` because the values and buckets are stored separately.

The average-case performance assumes that sorting each bucket is inexpensive, often because each bucket contains only a few values.

## Choosing `k`

`k` is the number of buckets. It is chosen based on the number of values, the input range, and how evenly the values are distributed.

Common choices include:

- `k = n`: a common choice when values are expected to be evenly distributed.
- `k = sqrt(n)`: a smaller-memory choice that works well for many practical inputs.
- Range-based buckets: choose a bucket width first, then calculate `k` from the input range.

For values in the range `[0, 1)`, a common bucket index is:

```python
index = int(value * k)
```

For general values between `minimum` and `maximum`, the index can be calculated as:

```python
index = int((value - minimum) * k / (maximum - minimum))
```

The index should be clamped to `k - 1` when a value can equal `maximum`.

There is a tradeoff:

- Too few buckets: buckets become large, so the sorting inside each bucket costs more.
- Too many buckets: many buckets remain empty, increasing memory and setup overhead.

The goal is to keep the values reasonably balanced across the buckets.

## Advantages

- Can be close to linear time for evenly distributed data.
- Easy to understand and implement.
- Useful when the input range and distribution are known.

## Disadvantages

- Performance depends on how evenly values are distributed.
- Requires extra memory for buckets.
- Not a good choice for highly skewed data.
- The bucket index calculation must match the input range.

## When to use Bucket Sort

Bucket Sort is useful for:

- Uniformly distributed decimal values.
- Data with a known and limited range.
- Large inputs where values can be distributed evenly.
- Grouping values into ranges before sorting them.

For arbitrary data, algorithms such as Merge Sort, Heap Sort, or Timsort are usually more reliable because their performance does not depend as strongly on the input distribution.
