/*
Clarifying Questions:
1) What makes a substring valid?
   → It must contain the same number of 0s and 1s, and all 0s must be consecutive and all 1s must be consecutive
     (i.e., the substring consists of exactly two adjacent groups like 000111 or 111000).
2) Are we counting substrings (contiguous) or subsequences?
   → Substrings (contiguous).
3) If the same substring appears multiple times, do we count all occurrences?
   → Yes.
4) What are the constraints?
   → 1 <= s.length <= 1e5, s[i] ∈ {'0','1'}.
5) What complexity is needed?
   → O(n) time is expected due to the size limit.

Example (Manual Walkthrough):
Input: s = "00110011"

Step 0 (start):
• prev = 0 (length of previous group)
• curr = 1 (length of current group, starting with s[0])
• result = 0

Step 1: i=1 (s[1]=0, s[0]=0)
• Rule/choice: Same char → extend current group
• After operation: curr=2, prev=0, result=0

Step 2: i=2 (s[2]=1, s[1]=0)
• Rule/choice: Char changed → group boundary found
• After operation:
  - result += min(prev, curr) = min(0,2)=0 → result=0
  - prev = curr → prev=2
  - curr = 1 (new group starts) → curr=1

Step 3: i=3 (s[3]=1, s[2]=1)
• Rule/choice: Same char → extend current group
• After operation: curr=2, prev=2, result=0

Step 4: i=4 (s[4]=0, s[3]=1)
• Rule/choice: Char changed → group boundary found
• After operation:
  - result += min(2,2)=2 → result=2
  - prev=2
  - curr=1

Step 5: i=5 (s[5]=0, s[4]=0)
• Rule/choice: Same char → extend current group
• After operation: curr=2, prev=2, result=2

Step 6: i=6 (s[6]=1, s[5]=0)
• Rule/choice: Char changed → group boundary found
• After operation:
  - result += min(2,2)=2 → result=4
  - prev=2
  - curr=1

Step 7: i=7 (s[7]=1, s[6]=1)
• Rule/choice: Same char → extend current group
• After operation: curr=2, prev=2, result=4

Stop condition met because: i reached the end of the string (loop finished).
Final add (last boundary contribution):
• result += min(prev, curr) = min(2,2)=2 → result=6
Answer for example: 6

Edge Cases:
• Already in target state:
  - Only one group (e.g., "0000" or "111") → no boundary → answer 0.
• Small n cases (n=1, n=2):
  - n=1 → 0
  - n=2 → "01" or "10" → 1, otherwise 0
• Negatives / duplicates:
  - Not applicable; duplicates are counted as separate occurrences.
• Tie-break scenario:
  - Not applicable.
• Overflow risk (int vs long):
  - n ≤ 1e5, result ≤ n-1 → int is safe.
• Any tricky case:
  - Must add the final min(prev,curr) after the loop, otherwise the last pair is missed.

Solution (Approach):
Idea (1-3 sentences):
• Scan the string once and compress it into consecutive groups (runs) of equal characters.
• For every adjacent pair of groups with lengths a and b, we can form exactly min(a, b) valid substrings.
• Sum these minima over all adjacent pairs.

Data Structure Choice:
• Using: Constant variables (prev, curr, result)
• Because: We only need the lengths of the last two groups; no extra array/list is required.

Algorithm Steps:
1) Initialize prev=0, curr=1, result=0.
2) For i from 1 to n-1:
   - If s[i] == s[i-1], increment curr.
   - Else (boundary):
     a) result += min(prev, curr)
     b) prev = curr
     c) curr = 1
3) After the loop, add result += min(prev, curr).
4) Return result.

Correctness (Why it works):
• Any valid substring must cross exactly one boundary between two adjacent groups (e.g., ...000|111...).
• If the left group has length a and the right group has length b, we can choose k=1..min(a,b) characters from each side
  to form a valid substring; thus there are min(a,b) valid substrings for that boundary.
• The algorithm finds every boundary once and adds its exact contribution, including the final boundary after the loop.

Complexity:
Time: O(n)
Space: O(1)

Implementation Notes:
• Helper methods: None (use Math.min).
• Tie-break handling: None.
• Index update pitfalls:
  - Start i at 1 because we compare with i-1.
  - Do not forget the final addition after the loop.
• Other notes:
  - curr starts at 1 because the first character begins the first group.
*/

class Solution {
    public int countBinarySubstrings(String s) {
        int prev = 0;   // length of previous group
        int curr = 1;   // length of current group (starts with s[0])
        int result = 0; // total valid substrings

        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == s.charAt(i - 1)) {
                curr++; // same group continues
            } else {
                result += Math.min(prev, curr); // add contribution of the boundary
                prev = curr; // shift current group to previous
                curr = 1;    // start new group
            }
        }

        // add contribution of the last boundary (last two groups)
        result += Math.min(prev, curr);

        return result;
    }
}