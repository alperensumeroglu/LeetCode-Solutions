/*
Clarifying Questions:
1) What exactly is a deci-binary number? 
   → A number whose digits are only 0 or 1 with no leading zeros.
2) Are we allowed to construct the deci-binary numbers themselves? 
   → No, we only need the minimum count.
3) What is the maximum length of the input string? 
   → Up to 10^5 digits.
4) Can the number contain digits other than 0–9? 
   → No, it consists only of decimal digits.
5) Do we need to return the actual partition or only the minimum number? 
   → Only the minimum number.

Example (Manual Walkthrough):
Input: n = "32"

Step 0 (start):
• Digits in n: 3, 2

Step 1:
• Rule/choice: Each deci-binary number can contribute at most 1 to any digit position.
• After operation: To build digit '3', we need at least 3 deci-binary numbers.

Step 2:
• Rule/choice: Check the maximum digit in the number.
• After operation: max digit = 3

Stop condition met because: The maximum digit determines the minimum number of deci-binary numbers needed.

Answer for example: 3

Edge Cases:
• Already in target state: If n only contains 0 and 1 → answer = 1
• Small n cases (n=1): result equals that digit
• Negatives / duplicates: not applicable
• Tie-break scenario: multiple digits may have same maximum
• Overflow risk (int vs long): none, since we only track digits
• Any tricky case: very long string (10^5 digits)

Solution (Approach):

Idea (1-3 sentences):
• Each deci-binary number can contribute at most '1' to each digit position.
• Therefore, to build a digit 'd', we need at least 'd' deci-binary numbers.
• The minimum number required equals the maximum digit in the string.

Data Structure Choice:
• Using: simple iteration over characters
• Because: we only need to track the maximum digit

Algorithm Steps:
1) Initialize max = 0
2) Iterate through each character in the string
3) Convert character digit to integer using (c - '0')
4) Update max = Math.max(max, digit)
5) Return max

Correctness (Why it works):
• A deci-binary number can add at most 1 per digit column.
• If a column contains digit 'd', at least 'd' numbers are required.
• The largest digit determines the minimum number of deci-binary numbers needed.

Complexity:
Time: O(n)
Space: O(1)

Implementation Notes:
• Helper methods: not required
• Tie-break handling: handled by tracking max
• Index update pitfalls: none
• Other notes: converting char to digit using (c - '0') is faster than parsing
*/

class Solution {
    public int minPartitions(String n) {

        int max = 0;

        for (char c : n.toCharArray()) {
            max = Math.max(max, c - '0');
        }

        return max;
    }
}