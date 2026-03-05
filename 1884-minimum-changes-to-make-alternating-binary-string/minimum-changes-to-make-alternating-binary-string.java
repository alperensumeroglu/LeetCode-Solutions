/*
Clarifying Questions:
1) Does the string contain only '0' and '1'? (Yes, guaranteed by constraints)
2) Can we flip any character in one operation? (Yes: '0' -> '1' or '1' -> '0')
3) Do we only need the minimum number of operations, not the resulting string? (Yes)
4) Is the string guaranteed to have at least one character? (Yes, length >= 1)
5) Is an alternating string defined strictly as no two adjacent characters being equal? (Yes)

Example (Manual Walkthrough):
Input: s = "0100"

Step 0 (start):
• Current string: 0100

Possible alternating targets:
Pattern1: 0101
Pattern2: 1010

Step 1:
• Rule/choice: Compare with Pattern1 (0101)
• After comparison:
index0: 0 vs 0 ✔
index1: 1 vs 1 ✔
index2: 0 vs 0 ✔
index3: 0 vs 1 ✘
Mismatch count = 1

Step 2:
• Rule/choice: Compare with Pattern2 (1010)
• After comparison:
index0: 0 vs 1 ✘
index1: 1 vs 0 ✘
index2: 0 vs 1 ✘
index3: 0 vs 0 ✔
Mismatch count = 3

Stop condition met because: all characters have been processed.

Answer for example: min(1,3) = 1

Edge Cases:
• Already in target state: "10", "01", "0101"
• Small n cases (n=1, n=2): a single character is already alternating
• Negatives / duplicates: not applicable (binary string)
• Tie-break scenario: both patterns require the same number of changes (e.g. "1111")
• Overflow risk (int vs long): none (n ≤ 10^4)
• Any tricky case: strings with all identical characters ("0000", "1111")

Solution (Approach):

Idea (1-3 sentences):
• An alternating binary string can only follow two patterns: "010101..." or "101010..."
• We iterate through the string once and count mismatches for both patterns.
• The minimum mismatch count equals the minimum number of operations required.

Data Structure Choice:
• Using: integer counters
• Because: we only need to track mismatch counts; no additional structure is needed.

Algorithm Steps:
1) Initialize two counters: count1 and count2
2) Traverse the string from left to right
3) For each index, determine expected characters for both patterns
4) Increment counters if the character does not match the expected pattern
5) Return the minimum of the two counters

Correctness (Why it works):
• There are only two valid alternating patterns for any binary string.
• Counting mismatches tells us how many flips are needed to convert to each pattern.
• Choosing the smaller count guarantees the minimum operations.

Complexity:
Time: O(n)
Space: O(1)

Implementation Notes:
• Helper methods: not required
• Tie-break handling: handled via Math.min()
• Index update pitfalls: ensure correct parity check using i % 2
• Other notes: charAt() provides efficient access
*/

class Solution {
    public int minOperations(String s) {

        int count1 = 0; // pattern: 010101...
        int count2 = 0; // pattern: 101010...

        for (int i = 0; i < s.length(); i++) {

            char c = s.charAt(i);

            if (i % 2 == 0) {
                if (c != '0') count1++;
                if (c != '1') count2++;
            } else {
                if (c != '1') count1++;
                if (c != '0') count2++;
            }
        }

        return Math.min(count1, count2);
    }
}