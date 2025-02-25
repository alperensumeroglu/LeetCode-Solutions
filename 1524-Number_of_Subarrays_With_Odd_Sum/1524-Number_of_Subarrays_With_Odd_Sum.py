class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7  # Define the modulo value
        
        result = 0  # Store the final count of subarrays with odd sum
        even_count = 1  # Count of subarrays with even prefix sum (including an implicit zero before array start)
        odd_count = 0  # Count of subarrays with odd prefix sum
        running_sum = 0  # Store the running sum of elements

        for num in arr:
            running_sum += num  # Update running sum
            
            if running_sum % 2 == 1:  # If running sum is odd
                result += even_count  # We can pair it with previously seen even prefix sums
                odd_count += 1  # Increase the count of odd prefix sums
            else:  # If running sum is even
                result += odd_count  # We can pair it with previously seen odd prefix sums
                even_count += 1  # Increase the count of even prefix sums
        
        return result % MOD  # Return the result modulo 10^9 + 7

'''

🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote

💡If this helped, don’t forget to upvote! 🚀🔥

**Intuition**
To count subarrays with an odd sum efficiently, we recognize that the parity of a sum determines its contribution. We use prefix sums to count how many odd and even sums we have encountered so far.

**Approach**
1. Use a running sum to track the cumulative sum as we iterate.
2. Maintain counters for even and odd prefix sums.
3. If the current sum is odd, it forms an odd subarray when combined with a previously seen even prefix sum.
4. If the current sum is even, it forms an odd subarray when combined with a previously seen odd prefix sum.
5. Update the count accordingly and return the result modulo \(10^9 + 7\).

**Complexity**
- Time complexity: $$O(n)$$ since we traverse the array once.
- Space complexity: $$O(1)$$ as we use only a few extra variables.

'''
