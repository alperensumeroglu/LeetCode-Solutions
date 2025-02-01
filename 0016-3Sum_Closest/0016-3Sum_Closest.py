# Problem: 16. 3Sum Closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the array to use the two-pointer technique
        nums.sort()
        closest_sum = float('inf')  # Initialize the closest sum with infinity

        # Iterate through the array
        for i in range(len(nums) - 2):
            left = i + 1  # Left pointer starts right after the current element
            right = len(nums) - 1  # Right pointer starts at the end of the array

            # Use the two-pointer technique
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # If the exact target is found, return it immediately
                if current_sum == target:
                    return current_sum

                # Update the closest sum if the current sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                # Adjust pointers based on the comparison with the target
                if current_sum < target:
                    left += 1  # Move the left pointer to increase the sum
                else:
                    right -= 1  # Move the right pointer to decrease the sum

        return closest_sum

"""

Intuition
This problem can be solved efficiently by sorting the array and using the two-pointer technique. Sorting allows us to leverage the relationship between the sum and the target to systematically adjust our pointers and find the closest sum.

Approach
1. Sort the input array to simplify pointer adjustments.
2. Use a fixed pointer (`i`) and two pointers (`left`, `right`) to form potential triplets.
3. Calculate the sum of the triplet and compare it to the target.
4. If the sum is exactly the target, return it immediately as the closest sum.
5. Otherwise, adjust the pointers based on whether the sum is less than or greater than the target.
6. Continue until all triplets are evaluated or the exact target sum is found.

Complexity
- Time complexity: $$O(n^2)$$
  Sorting the array takes $$O(n \log n)$$ and the two-pointer traversal takes $$O(n^2)$$.
- Space complexity: $$O(1)$$
  The solution uses constant extra space.

"""
