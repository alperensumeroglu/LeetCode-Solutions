
'''
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
1. We want to determine the minimum number of queries required to make `nums` a zero array.
2. Each query lets us decrement a range, and we can distribute decrements flexibly.
3.  We use binary search to efficiently find the smallest `k` that works.
# Approach
<!-- Describe your approach to solving the problem. -->
1. Use **binary search** on `k`, the number of queries applied.
2. For each `k`, use a **difference array** to efficiently apply range updates.
3. Use **prefix sum** to reconstruct the updated `nums`.
4. If any index in `nums` remains nonzero, discard that `k`.
5. The binary search ensures we find the minimal `k`.

**Time Complexity: O(n log m)**
- `can_make_zero_array(k)` runs in **O(n)** because:
  - We iterate over `k` queries: **O(k)**
  - We apply them using a **difference array**: **O(n)**
  - The worst case is when `k = m`, meaning **O(m + n) ≈ O(n)** (since `m ≤ n`)
- The **binary search** reduces the number of times `can_make_zero_array(k)` runs to **O(log m)**.
- **Total complexity** = **O(n log m)**
### **Space Complexity: O(n)**
- The only extra space used is:
  - **Difference array** (`diff`): **O(n + 1) ≈ O(n)**
  - Constant extra variables: **O(1)**
- **Total space complexity** = **O(n)**
'''
# Code
class Solution:
    def minZeroArray(self, nums, queries):
        """
        Finds the minimum number of queries needed to transform `nums` into a zero array.

        :param nums: List of integers representing the initial array.
        :param queries: List of queries where each query is [l, r, val].
        :return: Minimum k such that applying the first k queries makes `nums` a zero array.
        """
        
        n = len(nums)  # Array length
        
        def can_make_zero_array(k):
            """
            Checks if the first `k` queries can transform `nums` into a zero array.

            :param k: Number of queries to consider.
            :return: True if `nums` can be transformed to all zeros, else False.
            """
            diff = [0] * (n + 1)  # Difference array for efficient range updates
            
            # Apply the first `k` queries
            for i in range(k):
                left, right, val = queries[i]
                diff[left] += val
                diff[right + 1] -= val  # Subtract at right+1 to limit range update
            
            curr_val = 0  # Cumulative sum from difference array
            for i in range(n):
                curr_val += diff[i]  # Construct the modified array
                if curr_val < nums[i]:  # If we can't zero out an index
                    return False
            
            return True  # All elements can be reduced to zero
        
        # If `nums` is already zero, return 0
        if all(x == 0 for x in nums):
            return 0
        
        left, right = 1, len(queries)  # Binary search range
        
        # If applying all queries can't zero out `nums`, return -1
        if not can_make_zero_array(right):
            return -1
        
        # Binary search for the minimal `k`
        while left < right:
            mid = (left + right) // 2
            
            if can_make_zero_array(mid):  # Check if `mid` queries suffice
                right = mid  # Try a smaller `k`
            else:
                left = mid + 1  # Increase `k`
        
        return left  # Smallest valid `k`
