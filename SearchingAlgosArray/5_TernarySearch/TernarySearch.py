class TernarySearch:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def search(self):
        left = 0
        right = len(self.arr) - 1

        print(f"Starting ternary search for target {self.target}")
        print(f"Array: {self.arr}")

        while left <= right:
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3

            print(f"\nIteration: left={left}, right={right}")
            print(f"mid1={mid1}, arr[mid1]={self.arr[mid1]}")
            print(f"mid2={mid2}, arr[mid2]={self.arr[mid2]}")

            if self.arr[mid1] == self.target:
                print(f"Found target {self.target} at index {mid1}")
                return mid1

            if self.arr[mid2] == self.target:
                print(f"Found target {self.target} at index {mid2}")
                return mid2

            if self.target < self.arr[mid1]:
                print(f"Target is smaller than arr[mid1], search left part")
                right = mid1 - 1
            elif self.target > self.arr[mid2]:
                print(f"Target is greater than arr[mid2], search right part")
                left = mid2 + 1
            else:
                print(f"Target is between arr[mid1] and arr[mid2], search middle part")
                left = mid1 + 1
                right = mid2 - 1

        print(f"Target {self.target} not found.")
        return -1


# Example
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 11

result = TernarySearch(arr, target).search()
print(f"Final result: {result}")
