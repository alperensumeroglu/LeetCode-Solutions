# Solution for LeetCode Problem: 1726-Tuple_with_Same_Product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # Dictionary to count product pairs
        product_count = collections.Counter()
        n = len(nums)

        # Iterate over all pairs in nums to calculate product
        for i in range(n):
            for j in range(i):
                product_count[nums[i] * nums[j]] += 1

        # Initialize total count of valid tuples
        total_tuples = 0

        # For each product, calculate the number of valid tuples
        for count in product_count.values():
            if count > 1:
                # If there are count pairs, we can form C(count, 2) * 8 tuples
                total_tuples += (count * (count - 1) // 2) * 8

        return total_tuples


'''
Intuition
The problem revolves around identifying pairs of numbers that share the same product. 
If multiple pairs share the same product, we can derive valid tuples using these pairs.

Approach
1. Use a Counter to track the frequency of each product from all pairs of numbers in the array.
2. For each product that appears more than once, calculate the number of valid tuples using the formula:
   C(count, 2) * 8, where C(count, 2) is the number of ways to select 2 pairs from count pairs.
3. Sum up the tuples for all products to get the final result.

Complexity
- Time complexity: $$O(n^2)$$
  We iterate over all pairs in the array, resulting in a quadratic time complexity.
- Space complexity: $$O(n^2)$$
  In the worst case, the dictionary storing product counts could grow quadratically with the input size.

'''