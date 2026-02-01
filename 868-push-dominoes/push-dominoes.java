/*
Clarifying Questions:
1) Do we need to simulate dominoes second by second?
   -> No. The final state can be determined by distances between forces.
2) What happens if a domino is pushed from both sides?
   -> It stays upright due to balanced forces.
3) What if there is no force on one side?
   -> Sentinel forces are used to simplify edge cases.
4) Can we modify the input string directly?
   -> No. String is immutable; we construct the result separately.
5) Is there always a valid final state?
   -> Yes. The problem guarantees a valid result.

Example (Manual Walkthrough):
Input: ".L.R...LR..L.."

Step 0 (Add sentinels):
"L.L.R...LR..L..R"

Step 1:
Segment: L . L
Rule: Same forces (L...L)
Result: LL

Step 2:
Segment: L . R
Rule: Forces go outward (L...R)
Result: L.R

Step 3:
Segment: R ... L
Rule: Forces meet (R...L)
Result: RR.LL

Step 4:
Segment: L R
Rule: No dots between forces
Result: LR

Step 5:
Segment: R .. L
Rule: Forces meet (R...L)
Result: RRL

Final Output:
"LL.RR.LLRRLL.."

Edge Cases:
• Already stable input (e.g. "RR.L")
• Only dots (e.g. "....")
• Single domino
• All dominoes pushed in one direction
• Odd vs even number of dots between R and L

Solution (Approach):
Idea:
Process the dominoes segment by segment between force positions (L or R).
For each segment, determine the final state based on force directions.

Steps:
1) Add sentinel forces: 'L' at the beginning and 'R' at the end.
2) Scan the array to locate force positions.
3) For each segment between two forces:
   - Same forces → fill all with the same direction
   - L...R → keep dots unchanged
   - R...L → fill inward; middle stays upright if the count is odd
4) Build the final string using StringBuilder.

Data Structure Choice:
• char[] for direct character access
• StringBuilder for efficient string construction

Time Complexity:
• O(n) — single pass through the array

Space Complexity:
• O(n) — output string
*/

class Solution {
    public String pushDominoes(String dominoes) {
        // Add sentinel forces to handle edge cases
        char[] arr = ("L" + dominoes + "R").toCharArray();
        StringBuilder sb = new StringBuilder();

        int i = 0; // index of last seen force (L or R)

        for (int j = 1; j < arr.length; j++) {
            // Skip non-force positions
            if (arr[j] == '.') continue;

            int between = j - i - 1; // number of dots between forces
            char left = arr[i];
            char right = arr[j];

            // Append left force unless it is the sentinel
            if (i > 0) sb.append(left);

            if (left == right) {
                // Same direction forces: L...L or R...R
                for (int k = 0; k < between; k++) sb.append(left);
            } else if (left == 'L' && right == 'R') {
                // Forces go outward: L...R
                for (int k = 0; k < between; k++) sb.append('.');
            } else {
                // Forces meet: R...L
                int half = between / 2;
                for (int k = 0; k < half; k++) sb.append('R');
                if (between % 2 == 1) sb.append('.');
                for (int k = 0; k < half; k++) sb.append('L');
            }

            // Move to next segment
            i = j;
        }

        // Convert StringBuilder to String
        return sb.toString();
    }
}
