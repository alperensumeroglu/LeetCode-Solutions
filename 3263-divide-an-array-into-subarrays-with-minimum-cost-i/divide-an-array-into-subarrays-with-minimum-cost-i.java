/*
Clarifying Questions:
1) Do we need to explicitly build the three subarrays?
   -> No. Only the cost (first element of each subarray) matters.
2) Does the length of a subarray affect the cost?
   -> No. The cost depends only on the first element.
3) Is the first subarray always starting at index 0?
   -> Yes. Since subarrays must be contiguous, the first cost is nums[0].
4) Can we reorder the array?
   -> No. The array order must remain unchanged.
5) Is there always a valid way to split the array?
   -> Yes. The constraints guarantee n >= 3.

Example (Manual Walkthrough):
Input: nums = [10,3,1,1]

Step 0:
First subarray must start at index 0
Cost so far = 10

Remaining elements:
[3, 1, 1]

Step 1:
Choose the smallest value as the start of the second subarray -> 1

Step 2:
Choose the second smallest value as the start of the third subarray -> 1

Final Cost:
10 + 1 + 1 = 12

Edge Cases:
• Minimum length array (n = 3)
• All elements equal
• Strictly increasing array
• Strictly decreasing array

Solution (Approach):
Idea:
The cost of each subarray is determined only by its first element.
The first subarray always starts at nums[0].
To minimize the total cost, we should choose the two smallest possible
starting elements from nums[1..n-1] for the second and third subarrays.

Steps:
1) Take nums[0] as the cost of the first subarray.
2) Find the two smallest values in nums[1..n-1].
3) Add them to nums[0] to get the minimum total cost.

Data Structure Choice:
• Simple integer variables to track the two minimum values

Time Complexity:
• O(n) — single pass through the array

Space Complexity:
• O(1) — constant extra space
*/

class Solution {
    public int minimumCost(int[] nums) {
        int min1 = Integer.MAX_VALUE;
        int min2 = Integer.MAX_VALUE;

        // Find the two smallest values in nums[1..n-1]
        for (int i = 1; i < nums.length; i++) {
            int x = nums[i];

            if (x < min1) {
                min2 = min1;
                min1 = x;
            } else if (x < min2) {
                min2 = x;
            }
        }

        // First subarray cost is nums[0]
        return nums[0] + min1 + min2;
    }
}
