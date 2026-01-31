/*
Clarifying Questions:
1) Is the array `letters` guaranteed to be sorted in non-decreasing order?
2) Are there duplicates allowed in `letters` (e.g., ["x","x","y","y"])?  
3) Should the result be the smallest letter strictly greater than `target` (not >=)?
4) What should we return if no letter is strictly greater than `target`? (Wrap-around to letters[0]?)
5) What are the input constraints (array length) to justify O(log n) binary search?

Example (Manual Walkthrough):
Input: letters = ['c','f','j'], target = 'c'
Step 0 (start):
•  We need the smallest character strictly greater than 'c'. Initialize left=0, right=2, answer=-1.
Step 1:
•  Rule/choice: mid=1 -> letters[mid]='f'. Since 'f' > 'c', store answer=1 and search left half.
•  After operation: left=0, right=0, answer=1
Step 2:
•  Rule/choice: mid=0 -> letters[mid]='c'. Since 'c' <= 'c', discard left side and go right.
•  After operation: left=1, right=0, answer=1
Stop condition met because: left > right (search space exhausted)
Answer for example: letters[answer] = 'f'

Edge Cases:
•  Already in target state: If letters contains `target`, we still need the next greater (e.g., target='c' -> return 'f').
•  Small n cases (n=1, n=2): For n=2, binary search still works; if none greater, return letters[0].
•  Negatives / duplicates: Not applicable (chars), but duplicates are allowed; we must find the FIRST index with > target.
•  Tie-break scenario: Multiple letters > target (e.g., 'f' and 'j'); choose the smallest -> first qualifying index.
•  Overflow risk (int vs long): Use mid = left + (right - left) / 2 to avoid overflow.
•  Any tricky case: Wrap-around when target >= max letter (e.g., ['x','x','y','y'], target='z' -> return 'x').

Solution (Approach):
Idea (1-3 sentences):
•  Because `letters` is sorted, the set of indices where letters[i] > target forms a suffix.
•  We binary search for the first index where letters[i] > target.
•  If no such index exists, we return letters[0] due to wrap-around.

Data Structure Choice:
•  Using: Array + Binary Search (two pointers: left/right)
•  Because: Sorted array lets us discard half the search space each step (fast access by index, O(1)).
  (insert/delete/access tradeoff)

Algorithm Steps:
1) Initialize left=0, right=n-1, answer=-1.
2) While left <= right, compute mid safely.
3) If letters[mid] > target: set answer=mid and move right=mid-1 (search for a smaller valid index).
4) Else: move left=mid+1 (need a larger character).
5) After the loop, if answer==-1 return letters[0], otherwise return letters[answer].

Correctness (Why it works):
•  In a sorted array, if letters[mid] > target then every index >= mid is also > target, so mid is a candidate and the first such index (if any) lies on the left side.
•  If letters[mid] <= target, then every index <= mid cannot be an answer, so moving left to mid+1 cannot discard a valid solution.

Complexity:
Time: O(log n)
Space: O(1)

Implementation Notes:
•  Helper methods: None needed.
•  Tie-break handling: Always move `right` leftward when letters[mid] > target to ensure the first valid index.
•  Index update pitfalls: Use `left <= right` and update pointers correctly to avoid infinite loops.
•  Other notes: If `answer` stays -1, it means no letter is strictly greater than target, so wrap to letters[0].
*/
class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int left = 0;
        int right = letters.length - 1;
        int answer = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (letters[mid] > target) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return (answer == -1) ? letters[0] : letters[answer];
    }
}
