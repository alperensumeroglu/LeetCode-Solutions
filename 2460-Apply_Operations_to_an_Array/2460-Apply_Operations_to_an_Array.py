class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Step 1: Process the array by applying the given operations
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:  # If two adjacent numbers are equal
                nums[i] *= 2  # Multiply the first number by 2
                nums[i + 1] = 0  # Set the next number to 0
        
        # Step 2: Move all non-zero elements to the front
        idx = 0  # Pointer to place the non-zero elements
        for i in range(n):
            if nums[i] != 0:
                nums[idx] = nums[i]
                idx += 1
        
        # Step 3: Fill the rest of the array with zeros
        while idx < n:
            nums[idx] = 0
            idx += 1
        
        return nums

'''

🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote

💡If this helped, don’t forget to upvote! 🚀🔥

**Intuition**
The problem requires sequential operations on an array followed by rearranging elements. The goal is to ensure that when two adjacent numbers are equal, we double one and nullify the other. Finally, we shift all zeros to the end.

**Approach**
1. Iterate through the array:
   - If `nums[i]` is equal to `nums[i + 1]`, double `nums[i]` and set `nums[i + 1]` to zero.
2. Use a two-pointer approach to shift non-zero elements to the left.
3. Fill the remaining positions with zeros.

**Complexity**
- **Time Complexity:** O(n) → We traverse the array a constant number of times.
- **Space Complexity:** O(1) → The operations are performed in place without additional storage.

'''