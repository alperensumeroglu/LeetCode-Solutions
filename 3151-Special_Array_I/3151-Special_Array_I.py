class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        # Check if the array is empty or has one element
        if len(nums) <= 1:
            return True

        # Iterate through the array to check adjacent pairs for different parity
        for i in range(len(nums) - 1):
            # If two adjacent elements have the same parity, return False
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        
        # If all adjacent pairs have different parity, return True
        return True

"""

# Intuition
The problem is about checking the parity (odd/even) of adjacent elements in an array. If every pair of adjacent elements has different parity, the array is considered special.

# Approach
We iterate through the array and check every adjacent pair. If any pair of adjacent elements shares the same parity (both even or both odd), the array is not special, and we return `False`. If we finish the loop without finding such a pair, we return `True`.

# Complexity
- Time complexity: O(n), where n is the length of the array. We traverse the array once to check adjacent pairs.
- Space complexity: O(1), as we use a constant amount of space.
"""
