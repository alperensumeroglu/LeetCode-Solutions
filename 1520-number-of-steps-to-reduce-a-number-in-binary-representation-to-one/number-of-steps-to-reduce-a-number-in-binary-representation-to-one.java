/*
Clarifying Questions:
1) Are we allowed to convert the binary string to a decimal integer directly?
   → No need; length can be up to 500 bits (too large for built-in integer types).
2) What counts as a "step"?
   → Exactly one application of the rule: either +1 (if odd) or /2 (if even).
3) Is the input guaranteed to represent a positive integer and start with '1'?
   → Yes (s[0] == '1').
4) What is the target state?
   → Reduce the number to exactly "1".
5) Can we assume k (or steps) always terminates?
   → Yes, guaranteed we can reach 1 for all test cases.

Example (Manual Walkthrough):
Input: s = "1101"  (binary 13)

Step 0 (start):
• Current: 1101 (odd because last bit = 1)

Step 1:
• Rule/choice: odd → add 1
• After operation: 1101 + 1 = 1110

Step 2:
• Rule/choice: even → divide by 2
• After operation: 1110 / 2 = 111

Step 3:
• Rule/choice: odd → add 1
• After operation: 111 + 1 = 1000

Step 4:
• Rule/choice: even → divide by 2
• After operation: 1000 / 2 = 100

Step 5:
• Rule/choice: even → divide by 2
• After operation: 100 / 2 = 10

Step 6:
• Rule/choice: even → divide by 2
• After operation: 10 / 2 = 1

Stop condition met because: the value is now 1.
Answer for example: 6

Edge Cases:
• Already in target state: s = "1" → 0 steps
• Small n cases (length=1,2): "1" → 0, "10" → 1
• Negatives / duplicates: not applicable
• Tie-break scenario: not applicable
• Overflow risk (int vs long): yes if converting to decimal; avoid conversion
• Any tricky case: long suffix of '1's causes carry propagation (e.g., "111...")

Solution (Approach):
Idea (1-3 sentences):
• We simulate the process directly on the binary representation without converting to decimal.
• From right to left, we track a carry created by "+1" operations.
• Each processed bit contributes either 1 step (even case) or 2 steps (odd case: +1 then /2).

Data Structure Choice:
• Using: integer counters (steps, carry)
• Because: we only need O(1) state; no edits to the string are required.

Algorithm Steps:
1) Initialize steps = 0, carry = 0.
2) Iterate from the last bit down to index 1 (ignore index 0 for now).
3) Let bit = s[i] as 0/1. Consider effective value = bit + carry.
4) If effective value == 1 (odd): steps += 2 and set carry = 1.
5) Else (effective value 0 or 2, even): steps += 1.
6) Return steps + carry (extra step if carry affects the MSB).

Correctness (Why it works):
• Even numbers in binary end with 0, so dividing by 2 corresponds to removing the last bit (one step).
• Odd numbers end with 1; adding 1 makes the last bit 0 with possible carry, and then dividing by 2 removes it (two steps).
• The carry captures the impact of previous +1 operations on higher bits; adding carry at the end accounts for a final overflow at the MSB.

Complexity:
Time: O(L) where L = s.length
Space: O(1)

Implementation Notes:
• Helper methods: none
• Tie-break handling: not applicable
• Index update pitfalls: loop should run while i > 0 (do not process MSB inside loop)
• Other notes: convert char to int via (s.charAt(i) - '0')
*/

class Solution {
    public int numSteps(String s) {
        int steps = 0;
        int carry = 0;

        for (int i = s.length() - 1; i > 0; i--) {
            int bit = s.charAt(i) - '0';

            if (bit + carry == 1) { // odd
                steps += 2;         // +1, then /2
                carry = 1;          // carry propagates to the left
            } else {                // even (0 or 2)
                steps += 1;         // /2
            }
        }

        return steps + carry;
    }
}