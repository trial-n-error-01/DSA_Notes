class InterpolationSearch:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def search(self):
        low = 0
        high = len(self.arr) - 1

        print(f"Starting interpolation search for target {self.target}")
        print(f"Array: {self.arr}")

        while low <= high and self.arr[low] <= self.target <= self.arr[high]:
            print(f"\nIteration: low={low}, high={high}")

            if self.arr[low] == self.arr[high]:
                print(f"Checking last remaining value: arr[{low}] = {self.arr[low]}")
                if self.arr[low] == self.target:
                    print(f"Found target {self.target} at index {low}")
                    return low
                print(f"Target {self.target} not found.")
                return -1

            # Formula for estimated position
            pos = low + ((self.target - self.arr[low]) * (high - low)) // (self.arr[high] - self.arr[low])

            print(f"Estimated pos = {pos}")
            print(f"Compare arr[{pos}] = {self.arr[pos]} with target {self.target}")

            if self.arr[pos] == self.target:
                print(f"Found target {self.target} at index {pos}")
                return pos
            elif self.arr[pos] < self.target:
                print(f"Target is greater, move low from {low} to {pos + 1}")
                low = pos + 1
            else:
                print(f"Target is smaller, move high from {high} to {pos - 1}")
                high = pos - 1

        print(f"Target {self.target} not found in the array.")
        return -1


# Example
arr = [10, 20, 30, 40, 50, 60, 70, 80]
target = 60

result = InterpolationSearch(arr, target).search()
print(f"Target found at index: {result}")
