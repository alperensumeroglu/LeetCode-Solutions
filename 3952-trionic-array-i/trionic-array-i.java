/*
Clarifying Questions:
1) What does "trionic" mean?
   - The array must have three consecutive segments: strictly increasing, strictly decreasing, strictly increasing.
2) What are the constraints on p and q?
   - 0 < p < q < n-1, so each segment must contain at least two elements.
3) What does "strictly" imply?
   - No equality is allowed: use < for increasing and > for decreasing.
4) Do we need to find all possible (p, q)?
   - No, finding at least one valid split is sufficient.
5) Any performance constraints?
   - n ≤ 100, so an O(n) single-pass solution is optimal.

Example (Manual Walkthrough):
Input: [1, 3, 5, 4, 2, 6]
Step 0 (start):
• Goal: Traverse the array in three ordered phases.
Step 1:
• Phase 1 (increasing): 1 < 3 < 5 → peak at index p = 2
Step 2:
• Phase 2 (decreasing): 5 > 4 > 2 → valley at index q = 4
Step 3:
• Phase 3 (increasing): 2 < 6 and we reach the end → valid trionic array

Edge Cases:
• No initial increasing segment → false
• Increasing but never decreasing → false
• Decreasing but never increasing again → false
• Equal adjacent values (…, 3, 3, …) → false (violates strictly condition)
• Last segment has only one element (q == n-1) → false

Approach:
• Use a single pointer i to process the array in three phases:
  1) while nums[i] < nums[i+1]  (increasing)
  2) while nums[i] > nums[i+1]  (decreasing)
  3) while nums[i] < nums[i+1]  (increasing)
• Validate that each phase has length ≥ 2 (p > 0, q > p, q < n-1)
• Finally, ensure the entire array is consumed (i == n-1)

Time Complexity:
• O(n)

Space Complexity:
• O(1)
*/

class Solution {
    public boolean isTrionic(int[] nums) {
        int n = nums.length;
        if(n < 4) return false;

        int i = 0;
        // Strictly increasin nums[0..p]
        while(i + 1 < n && nums[i] < nums[i+1]) i++;
        int p = i;
        if(p == 0) return false;
        // strictly decvreasing nums[p..q]       
        while(i + 1 < n && nums[i] > nums[i+1]) i++;
        int q = i;
        if(p == q || q == n - 1) return false;
        //strictly increasing 
        while(i + 1 < n && nums[i] < nums[i+1]) i++;
        return i == n - 1;
     }
}