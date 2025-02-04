class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        n = len(nums)  # Length of the input array

        # Initialize a list to store the sum of ascending subarrays
        ascending_sums = [0] * n
        ascending_sums[0] = nums[0]  # The first element starts its own subarray

        max_sum = nums[0]  # Initialize the maximum sum to the first element

        # Iterate through the array starting from the second element
        for i in range(1, n):
            if nums[i] > nums[i - 1]:  # Check if the current element continues an ascending subarray
                ascending_sums[i] = ascending_sums[i - 1] + nums[i]
            else:
                ascending_sums[i] = nums[i]  # Start a new ascending subarray

            max_sum = max(max_sum, ascending_sums[i])  # Update the maximum sum if necessary

        return max_sum

'''
Intuition
The problem involves finding the maximum sum of contiguous ascending subarrays. If a number in the array is greater than the previous one, it can extend the existing subarray; otherwise, it starts a new subarray.

Approach
1. Iterate through the array to calculate the sum of ascending subarrays.
2. Use a helper list to track the current sum of each ascending subarray.
3. Compare and update the maximum sum found so far.

Complexity
- Time complexity: O(n), where n is the length of the input array, since we iterate through it once.
- Space complexity: O(n), for the additional list used to store the ascending subarray sums.
'''