def binary_search_recursive(arr, target, left, right, depth=0):
    indent = "  " * depth

    if left > right:
        print(indent + "Empty branch")
        return -1

    mid = left + (right - left) // 2
    root = arr[mid]

    print(indent + f"Root: {root}")
    print(indent + "   / \\")

    left_segment = arr[left:mid] if left < mid else []
    right_segment = arr[mid + 1:right + 1] if mid < right else []

    left_text = str(left_segment) if left_segment else ""
    right_text = str(right_segment) if right_segment else ""
    print(indent + f" {left_text:<20} {right_text}")

    if arr[mid] == target:
        print(indent + f"Found {target} at index {mid}")
        return mid

    if arr[mid] < target:
        print(indent + "Go right")
        return binary_search_recursive(arr, target, mid + 1, right, depth + 1)
    else:
        print(indent + "Go left")
        return binary_search_recursive(arr, target, left, mid - 1, depth + 1)


# Example usage
numbers = [2, 5, 8, 12, 16, 23, 38, 45, 57]
print("Binary Search Tree Style")
print("         16")
print("       /    \\")
print("      5      38")
print("     / \\    /  \\")
print("    2  12  23   45")
print("         /          \\")
print("        8           57")
print()

result = binary_search_recursive(numbers, 23, 0, len(numbers) - 1)

if result != -1:
    print(f"\nFinal result: index {result}")
else:
    print("\nFinal result: not found")
