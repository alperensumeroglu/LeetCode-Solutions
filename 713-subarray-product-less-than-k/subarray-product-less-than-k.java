/*
Clarifying Questions:
1) Is “subarray” required to be contiguous? (Yes, contiguous by definition.)
2) Are all nums[i] positive? (Yes: 1 <= nums[i] <= 1000, crucial for sliding window.)
3) Is the condition strictly less than k (< k) or <= k? (Strictly less than k.)
4) What if k <= 1? (Answer is 0 because product of positive ints is always >= 1.)
5) Do we return the subarrays or just the count? (Just the count.)

Example (Manual Walkthrough):
Input: nums = [10, 5, 2, 6], k = 100

Step 0 (start):
•  left = 0, prod = 1, count = 0

Step 1 (right = 0, x = 10):
•  Rule/choice: expand window => prod *= 10 => prod = 10 (<100)
•  After operation: valid subarrays ending at right=0 are (right-left+1)=1
  count = 1

Step 2 (right = 1, x = 5):
•  Rule/choice: expand window => prod *= 5 => prod = 50 (<100)
•  After operation: valid endings = (1-0+1)=2  -> [5], [10,5]
  count = 3

Step 3 (right = 2, x = 2):
•  Rule/choice: expand window => prod *= 2 => prod = 100 (>=100) -> shrink
•  After operation (shrink): prod /= nums[left]=10 => prod=10, left=1 (<100)
  valid endings = (2-1+1)=2 -> [2], [5,2]
  count = 5

Step 4 (right = 3, x = 6):
•  Rule/choice: expand window => prod *= 6 => prod = 60 (<100)
•  After operation: valid endings = (3-1+1)=3 -> [6], [2,6], [5,2,6]
  count = 8

Stop condition met because: right reached nums.length - 1
Answer for example: 8

Edge Cases:
•  Already in target state: if k is very large, almost all subarrays count (still must compute).
•  Small n cases (n=1, n=2): handle naturally; for n=1 count is 1 if nums[0] < k else 0.
•  Negatives / duplicates: negatives do NOT exist here; duplicates are fine.
•  Tie-break scenario: not applicable (we count, not choose).
•  Overflow risk (int vs long): use long for prod to avoid overflow during multiplication.
•  Any tricky case: k <= 1 => immediately return 0; repeated shrinking when prod grows too big.

Solution (Approach):
Idea (1-3 sentences):
•  Use a sliding window [left..right] with a running product.
•  Expand right; while product >= k, shrink from left by dividing out nums[left].
•  Once product < k, every subarray ending at right and starting from any index in [left..right] is valid.

Data Structure Choice:
•  Using: two pointers (left, right) + running product (long)
•  Because: with all-positive numbers, expanding increases product and shrinking decreases it,
  enabling O(1) updates and O(n) total moves.

Algorithm Steps:
1) If k <= 1 return 0.
2) Initialize left=0, prod=1, count=0.
3) For right from 0 to n-1: multiply prod by nums[right].
4) While prod >= k: divide prod by nums[left], increment left.
5) Add (right - left + 1) to count (valid subarrays ending at right). Return count.

Correctness (Why it works):
•  With all nums[i] > 0, shrinking the window (moving left forward) monotonically decreases prod,
  so the while-loop finds the smallest left such that prod < k for each right.
•  When prod < k, any start index s in [left..right] gives a subarray nums[s..right] whose product
  is <= prod < k (removing positive factors only decreases the product), so there are (right-left+1) valid subarrays.

Complexity:
Time: O(n) (each pointer moves forward at most n times)
Space: O(1) extra space

Implementation Notes:
•  Helper methods: none needed
•  Tie-break handling: not applicable
•  Index update pitfalls: make sure to shrink while (prod >= k), and add count AFTER shrinking
•  Other notes: strict inequality matters; [10,5,2] product=100 is NOT counted when k=100
*/

class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k <= 1) return 0;

        long prod = 1;
        int left = 0;
        int count = 0;

        for (int right = 0; right < nums.length; right++) {
            prod *= nums[right];

            while (prod >= k && left <= right) {
                prod /= nums[left];
                left++;
            }

            count += (right - left + 1);
        }

        return count;
    }
}