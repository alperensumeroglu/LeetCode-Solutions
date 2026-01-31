/*
Clarifying Questions:
1) Are we asked to return the number of distinct elements with maximum frequency, or the SUM of their frequencies?
2) Do duplicates count as separate occurrences in the sum? (Yes, frequency means occurrences.)
3) Are nums always positive integers as stated? (Yes, but solution works regardless.)
4) Any constraints that require optimizing beyond HashMap counting? (n is small; O(n) is fine.)
5) If multiple values tie for maximum frequency, do we include all of them in the total? (Yes.)

Example (Manual Walkthrough):
Input: nums = [1,2,2,3,1,4]
Step 0 (start):
•  Count frequencies of each number.
Step 1:
•  Rule/choice: build freqMap = {1:2, 2:2, 3:1, 4:1}
•  After operation: maxFreq not computed yet
Step 2:
•  Rule/choice: find maxFreq = 2, then sum all frequencies equal to maxFreq
•  After operation: result = 2 (for 1) + 2 (for 2) = 4
Stop condition met because: all map entries processed
Answer for example: 4

Edge Cases:
•  Already in target state: all elements identical -> answer = n (only one element has max frequency n)
•  Small n cases (n=1, n=2): max frequency is 1 or 2; result becomes n
•  Negatives / duplicates: duplicates are the whole point; negatives not in constraints but still work
•  Tie-break scenario: if multiple elements share maxFreq, we include ALL of them in the sum
•  Overflow risk (int vs long): n is small; int is safe (result <= n)
•  Any tricky case: when all frequencies are 1, result should be the length of the array

Solution (Approach):
Idea (1-3 sentences):
•  Use a HashMap to count how many times each number appears.
•  Compute the maximum frequency among all numbers.
•  Sum the frequencies of every number whose frequency equals that maximum.

Data Structure Choice:
•  Using: HashMap<Integer, Integer>
•  Because: we need fast counting by value (O(1) average updates/lookups) and then iterate frequencies
  (insert/delete/access tradeoff)

Algorithm Steps:
1) Create an empty HashMap freqMap.
2) For each num in nums, do freqMap[num]++ using getOrDefault.
3) Iterate freqMap values to find maxFreq.
4) Iterate freqMap values again and add freq to result if freq == maxFreq.
5) Return result.

Correctness (Why it works):
•  freqMap stores the exact occurrence count for each distinct number, so frequencies are correct.
•  maxFreq is the largest frequency present; summing all frequencies equal to maxFreq returns exactly the total occurrences of all max-frequency elements.

Complexity:
Time: O(n)   (plus O(k) over distinct values; k <= n)
Space: O(k)  (HashMap for distinct numbers)

Implementation Notes:
•  Helper methods: none needed
•  Tie-break handling: handled by summing all freq == maxFreq
•  Index update pitfalls: none; avoid modifying the map while iterating over values
•  Other notes: return is not the count of distinct max elements; it is the SUM of their frequencies
*/

class Solution {
    public int maxFrequencyElements(int[] nums) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        int maxFreq = 0;
        int result = 0;

        for(int num : nums) {
            int freq = freqMap.getOrDefault(num, 0) + 1;
            freqMap.put(num, freq);

            if(freq > maxFreq) {
                maxFreq = freq;
                result = freq;
            } else if(freq == maxFreq){
                result += freq;
            }
        }   
        return result;

         }
}