
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # Initialize pointers for binary search
        left, right = 0, len(nums) - 1

        # Perform binary search
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2

            # Check if the target is at the mid index
            if nums[mid] == target:
                return mid

            # If the target is greater, move the left pointer to mid + 1
            elif target > nums[mid]:
                left = mid + 1

            # If the target is smaller, move the right pointer to mid - 1
            else:
                right = mid - 1

        # If target is not found, return the insertion position
        return left

'''

Intuition
The problem requires finding the position of a target value in a sorted array, or determining where it can be inserted while maintaining order. The sorted nature of the array suggests the use of a binary search algorithm for efficiency.

Approach
1. Use two pointers, left and right, to define the current search space within the array.
2. Calculate the mid-point of the current search range.
3. Compare the target value with the value at the mid-point:
   - If the target equals the mid-point value, return the mid index.
   - If the target is greater, narrow the search to the right half.
   - If the target is smaller, narrow the search to the left half.
4. If the target is not found, the left pointer will indicate the correct insertion index.

Complexity
- Time complexity: O(log n) because the binary search divides the search space by half in each iteration.
- Space complexity: O(1) since the solution uses only a constant amount of extra space.

'''