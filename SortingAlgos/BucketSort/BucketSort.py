from typing import List


def bucket_sort(values: List[float]) -> List[float]:
    """Sort decimal values in the range [0, 1) using Bucket Sort."""
    if not values:
        return []

    bucket_count = len(values)
    buckets: List[List[float]] = [[] for _ in range(bucket_count)]

    for value in values:
        if not 0 <= value < 1:
            raise ValueError("Bucket Sort example expects values in the range [0, 1)")

        bucket_index = min(int(value * bucket_count), bucket_count - 1)
        buckets[bucket_index].append(value)

    print(f"Buckets after distribution: {buckets}")

    for bucket in buckets:
        bucket.sort()

    print(f"Buckets after sorting: {buckets}")

    sorted_values = [value for bucket in buckets for value in bucket]
    return sorted_values


if __name__ == "__main__":
    numbers = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
    print(f"Input: {numbers}")

    result = bucket_sort(numbers)

    print(f"Sorted output: {result}")
