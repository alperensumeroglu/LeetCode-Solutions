class Solution:
    def maximumSum(self, nums):
        # Dictionary to store the maximum number for each digit sum
        digit_sum_map = {}
        max_sum = -1

        # Iterate over the numbers to compute the digit sum
        for num in nums:
            digit_sum = 0
            temp = num

            # Compute sum of digits manually (without using sum() or map())
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10

            # If a number with the same digit sum exists, calculate max pair sum
            if digit_sum in digit_sum_map:
                max_sum = max(max_sum, digit_sum_map[digit_sum] + num)

            # Store the maximum number encountered for the current digit sum
            digit_sum_map[digit_sum] = max(digit_sum_map.get(digit_sum, 0), num)

        return max_sum


'''
Intuition
This problem requires us to find two numbers with the same digit sum and maximize their sum. 
A brute force approach would compare all pairs, but we can optimize using a hashmap.

Approach
1. Use a dictionary to map the sum of digits of numbers to the maximum number found with that sum.
2. Iterate through the array:
   - Compute the sum of digits of the current number manually (without using sum()).
   - If another number with the same digit sum exists, update the maximum possible sum.
   - Store the largest number encountered for each digit sum.
3. Return the maximum sum found or -1 if no such pair exists.

Complexity
- Time complexity: O(n) → We iterate through the list once and perform O(1) operations for each element.
- Space complexity: O(n) → In the worst case, we store all unique digit sums in the dictionary.

'''
