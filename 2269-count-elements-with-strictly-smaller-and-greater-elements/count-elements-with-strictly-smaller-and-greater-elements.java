/*
Clarifying Questions:
1) Do we count an element if there exists at least one strictly smaller AND at least one strictly greater value in the array?
2) Does "strictly" mean using < and > (no equality allowed)?
3) Do duplicates count separately if they satisfy the condition (e.g., two 3's both counted)?
4) Are we allowed to reorder the array / use sorting, or should we prefer O(n) scanning?
5) Any constraints on time/space (n up to 100, so O(n) is fine, but we can do O(n) easily)?

Example (Manual Walkthrough):
Input: nums = [11, 7, 2, 15]
Step 0 (start):
•  Find global min and max.
Step 1:
•  Rule/choice: compute min=2, max=15
•  After operation: min=2, max=15
Step 2:
•  Rule/choice: count elements where min < num < max
•  After operation: counted {7, 11}
Stop condition met because: all elements processed
Answer for example: 2

Edge Cases:
•  Already in target state: if all elements are equal (min == max) -> answer is 0
•  Small n cases (n=1, n=2): no element can have both smaller and greater -> 0
•  Negatives / duplicates: handled naturally; duplicates can be counted if strictly between min and max
•  Tie-break scenario: N/A (no tie-breaking needed)
•  Overflow risk (int vs long): none; only comparisons, no multiplication/sums
•  Any tricky case: when min == max, the condition (num > min && num < max) is impossible

Solution (Approach):
Idea (1-3 sentences):
•  The only elements that qualify are those strictly between the array's global minimum and maximum.
•  First compute min and max in one pass, then count how many values satisfy min < x < max.
•  Duplicates in the middle are counted individually.

Data Structure Choice:
•  Using: two integers (min, max) + an integer counter
•  Because: we only need global boundaries and a count; no extra structure improves this
  (insert/delete/access tradeoff)

Algorithm Steps:
1) Initialize min and max as nums[0]
2) Loop over nums: update min = Math.min(min, num), max = Math.max(max, num)
3) Initialize count = 0
4) Loop over nums again: if (num > min && num < max) count++
5) Return count

Correctness (Why it works):
•  Any element equal to min cannot have a strictly smaller element; any element equal to max cannot have a strictly greater element.
•  Any element x with min < x < max has at least one strictly smaller (min) and one strictly greater (max), so it must be counted.

Complexity:
Time: O(n)
Space: O(1)

Implementation Notes:
•  Helper methods: none needed
•  Tie-break handling: none
•  Index update pitfalls: none (simple loops)
•  Other notes: can early return 0 when min == max, but not required
*/

class Solution {
    public int countElements(int[] nums) {
        int min = nums[0];
        int max = nums[0];

        for(int num : nums){
            min = Math.min(min, num);
            max = Math.max(max, num);
        }

        int count = 0;
        for(int num : nums) {
            if(num > min && num < max) {
                count++;
            }
        }
        return count;
    }
}