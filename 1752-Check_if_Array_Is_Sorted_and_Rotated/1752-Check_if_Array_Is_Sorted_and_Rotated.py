class Solution:
    def check(self, nums: list[int]) -> bool:
        # Initialize a counter for violations (number of descending order points)
        violation_count = 0

        # Iterate through the array and check if the current element is greater than the next (circularly)
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                violation_count += 1

        # Return true if there is at most one violation, indicating a sorted and rotated array
        return violation_count <= 1
'''
# Intuition
The problem checks whether a given array was sorted in non-decreasing order and then rotated. 
To identify this, we need to check if the array has at most one "violation," where a number is greater than its subsequent number (in circular order).

# Approach
1. Traverse the array while comparing each element to the next element (using modulo for circular comparison).
2. Count the number of violations (where the current number is greater than the next).
3. If the number of violations is at most one, the array is sorted and rotated.

# Complexity
- Time complexity: O(n), where n is the length of the array, as we traverse it once.
- Space complexity: O(1), as no additional space is used.
'''