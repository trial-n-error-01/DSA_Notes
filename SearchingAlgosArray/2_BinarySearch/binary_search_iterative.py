def binary_search_iterative(arr, target):
    left = 0
    right = len(arr) - 1

    print(f"Searching for {target} in {arr}")

    while left <= right:
        mid = left + (right - left) // 2
        print(f"\nCurrent search space: arr[{left}:{right}] -> {arr[left:right+1]}")
        print(f"Middle index = {mid}, middle value = {arr[mid]}")

        if arr[mid] == target:
            print(f"Found {target} at index {mid}")
            return mid
        elif arr[mid] < target:
            print(f"{target} is greater than {arr[mid]}, moving right")
            left = mid + 1
        else:
            print(f"{target} is smaller than {arr[mid]}, moving left")
            right = mid - 1

    print(f"{target} not found in the array")
    return -1


# Example usage
numbers = [2, 5, 8, 12, 16, 23, 38, 45, 57]
result = binary_search_iterative(numbers, 23)

if result != -1:
    print(f"Final index: {result}")
else:
    print("Final result: not found")
