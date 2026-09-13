def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
numbers = [8, 3, 12, 5, 9]
search_value = 12

result = linear_search(numbers, search_value)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found")
