/*
Clarifying Questions:
1) Are we expected to construct the full string Sn? (No, it would be too large.)
2) Is k guaranteed to be valid for the given n? (Yes, problem statement guarantees this.)
3) What is the maximum size of Sn? (Length = 2^n - 1)
4) Are characters strictly binary ('0' and '1')? (Yes)
5) Can recursion be used since n ≤ 20? (Yes, recursion depth is small.)

Example (Manual Walkthrough):
Input: n = 3, k = 6

Step 0 (start):
• S3 = "0111001"
• length = 7
• mid = 4

Step 1:
• Rule/choice: k > mid → we are in the RIGHT part
• mirror index = len - k + 1 = 7 - 6 + 1 = 2
• So we check the mirrored position in S2

Step 2:
• Rule/choice: findKthBit(2, 2)
• S2 = "011"
• bit = '1'

RIGHT part is reverse(invert(LEFT)), so we invert:
• '1' → '0'

Stop condition met because: recursion reaches base case (n == 1)

Answer for example: "0"

Edge Cases:
• Already in target state: not applicable since string is generated
• Small n cases (n=1, n=2): handled directly (base case returns '0')
• Negatives / duplicates: not applicable
• Tie-break scenario: middle element always '1'
• Overflow risk (int vs long): safe since n ≤ 20
• Any tricky case: k exactly at the middle index

Solution (Approach):

Idea (1-3 sentences):
• The string Sn has a recursive symmetric structure:
  Sn = S(n-1) + "1" + reverse(invert(S(n-1))).
• Instead of building the entire string, we exploit this symmetry.
• If k is in the right half, we mirror it to the left half and invert the result.

Data Structure Choice:
• Using: recursion with integers
• Because: the problem naturally reduces from Sn to S(n-1)

Algorithm Steps:
1) Compute length of Sn → len = 2^n - 1
2) Find middle index → mid = len / 2 + 1
3) If k == mid → return '1'
4) If k < mid → recursively check S(n-1)
5) If k > mid → mirror index and invert the result

Correctness (Why it works):
• Sn consists of a left part, a fixed middle bit, and a right part
• The right part is the reversed and inverted version of the left part
• Using mirror mapping and inversion allows us to locate the correct bit without building the string

Complexity:
Time: O(n)
Space: O(n) (recursion stack)

Implementation Notes:
• Helper methods: recursion handled in same function
• Tie-break handling: middle index directly returns '1'
• Index update pitfalls: mirror calculation = len - k + 1
• Other notes: use bit shift (1 << n) to compute 2^n efficiently
*/

class Solution {

    public char findKthBit(int n, int k) {

        if (n == 1) return '0';

        int len = (1 << n) - 1;
        int mid = len / 2 + 1;

        if (k == mid) return '1';

        if (k < mid) {
            return findKthBit(n - 1, k);
        }

        char bit = findKthBit(n - 1, len - k + 1);
        return bit == '0' ? '1' : '0';
    }
}