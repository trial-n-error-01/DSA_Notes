class JumpSearch:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def search(self):
        n = len(self.arr)
        if n == 0:
            print("Array is empty. Returning -1.")
            return -1

        step = int(n ** 0.5)
        prev = 0

        print(f"Starting jump search for target {self.target} in array of length {n}")
        print(f"Array: {self.arr}")
        print(f"Initial step size: {step}")

        while prev < n and self.arr[min(step, n) - 1] < self.target:
            print(f"\nJump iteration:")
            print(f"prev = {prev}, step = {step}")
            print(f"Compare arr[{min(step, n) - 1}] = {self.arr[min(step, n) - 1]} with target {self.target}")

            prev = step
            step += int(n ** 0.5)

            print(f"Move prev to {prev} and increase step to {step}")

            if prev >= n:
                print("Target not found in the array. Returning -1.")
                return -1

        print(f"\nLinear scan block: from index {prev} to {min(step, n) - 1}")

        for i in range(prev, min(step, n)):
            print(f"Checking index {i}: value = {self.arr[i]}")
            if self.arr[i] == self.target:
                print(f"Found target {self.target} at index {i}")
                return i

        print(f"Target {self.target} not found in the scanned block.")
        return -1


# Example
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 15

print("\nRunning Jump Search...\n")
result = JumpSearch(arr, target).search()
print(f"\nFinal result: {result}")