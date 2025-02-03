
class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        n = len(nums)

        # longest_increasing[i] stores the length of the longest strictly increasing subarray ending at index i
        longest_increasing = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                longest_increasing[i] = longest_increasing[i - 1] + 1

        # longest_decreasing[i] stores the length of the longest strictly decreasing subarray ending at index i
        longest_decreasing = [1] * n
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                longest_decreasing[i] = longest_decreasing[i - 1] + 1

        # Return the maximum of the longest strictly increasing or strictly decreasing subarrays
        return max(max(longest_increasing), max(longest_decreasing))

'''

Intuition
To solve this problem, we need to find the longest subarray that is either strictly increasing or strictly decreasing. 
A dynamic programming approach can efficiently track the lengths of such subarrays as we traverse the array.

Approach
1. Create two arrays:
   - `longest_increasing` to store the lengths of the longest strictly increasing subarrays ending at each index.
   - `longest_decreasing` to store the lengths of the longest strictly decreasing subarrays ending at each index.
2. Iterate through the input array:
   - Update `longest_increasing` if the current element is greater than the previous element.
   - Update `longest_decreasing` if the current element is less than the previous element.
3. Return the maximum value from both arrays, representing the longest subarray that is either strictly increasing or strictly decreasing.

Complexity
- Time complexity: O(n), where n is the length of the input array. We traverse the array twice.
- Space complexity: O(n), due to the two auxiliary arrays `longest_increasing` and `longest_decreasing`.

'''