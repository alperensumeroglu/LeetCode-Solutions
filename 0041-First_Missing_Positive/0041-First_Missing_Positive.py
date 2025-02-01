class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Step 1: Replace all negative numbers and zeros with a placeholder value (0)
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = 0

        # Step 2: Use the array itself to indicate presence of numbers
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                # Mark the presence of 'val' in the array by making nums[val-1] negative
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)

        # Step 3: Find the first positive index, which corresponds to the missing number
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i

        # If all numbers from 1 to len(nums) are present, return len(nums) + 1
        return len(nums) + 1

'''

# Intuition
To find the smallest missing positive integer, we can use the input array itself to store information about the presence of numbers, avoiding extra space usage.

# Approach
1. Replace all negative numbers and zeros in the array with 0 since they do not contribute to the solution.
2. Use the indices of the array to track the presence of numbers from 1 to `len(nums)`:
   - For each value `val` in the array, if `1 <= val <= len(nums)`, mark `nums[val - 1]` as negative to indicate that `val` is present.
3. Iterate over the modified array to find the first index `i` where the value is non-negative. The missing integer is `i + 1`.
4. If all indices are marked, the smallest missing positive integer is `len(nums) + 1`.

# Complexity
- Time complexity: $$O(n)$$, since we traverse the array a constant number of times.
- Space complexity: $$O(1)$$, as no additional space is used apart from the input array.

'''