class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # Initialize variables to track the minimum subarray sum, maximum subarray sum, and the final answer
        min_subarray_sum = 0  
        max_subarray_sum = 0
        result = 0

        # Iterate through the given list
        for num in nums:
            # Update maximum subarray sum using Kadane's algorithm
            max_subarray_sum = max(num, num + max_subarray_sum)

            # Update minimum subarray sum using Kadane's algorithm (negative version)
            min_subarray_sum = min(num, num + min_subarray_sum)

            # Keep track of the maximum absolute sum found so far
            result = max(result, abs(max_subarray_sum), abs(min_subarray_sum))

        return result


'''
🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote

💡If this helped, don’t forget to upvote! 🚀🔥

## Intuition
To find the maximum absolute sum of any subarray, we need to track both the maximum subarray sum and the minimum subarray sum.
The maximum absolute sum will be the largest absolute value between them.

## Approach
We use **Kadane's algorithm** twice:
1. First, to find the **maximum subarray sum** (standard Kadane's algorithm).
2. Second, to find the **minimum subarray sum**, which is done by applying Kadane's algorithm but tracking the minimum instead.
3. The result is the maximum absolute value of these two.

## Complexity
• Time complexity: O(n) - We iterate through the list once.
• Space complexity: O(1) - We use a few extra variables but no additional data structures.
'''
