def binary_search(arr, low, high, target):
    while low <= high:
        mid = low + (high - low) // 2
        print(f"Binary search: low={low}, high={high}, mid={mid}, value={arr[mid]}")

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def exponential_search(arr, target):
    n = len(arr)

    if n == 0:
        return -1

    if arr[0] == target:
        return 0

    index = 1
    print(f"Finding range: start index = {index}")

    while index < n and arr[index] < target:
        print(f"Check index {index}: value = {arr[index]}")
        index *= 2

    low = index // 2
    high = min(index, n - 1)

    print(f"Target range found: low={low}, high={high}")
    return binary_search(arr, low, high, target)


# Example
arr = [2, 3, 4, 10, 40, 50, 70, 90, 100]
target = 50

result = exponential_search(arr, target)
print(f"Final result: {result}")
