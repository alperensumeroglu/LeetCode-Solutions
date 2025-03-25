class Solution:
    def checkValidCuts(self, n, rectangles):
            return self.can_cut(rectangles, 0) or self.can_cut(rectangles, 1)
    """
    💡 Intuition:
    We are given a list of axis-aligned rectangles.
    The goal is to determine if we can draw *at least 3* non-overlapping vertical or horizontal lines (cuts)
    that each intersect at least one rectangle.

    🧠 Approach:
    1. We check both vertical and horizontal axes (0 for x, 1 for y).
    2. For each axis:
        a. Sort the rectangles based on their start coordinate along that axis.
        b. Iterate through rectangles and keep track of the farthest "end" of previously checked rectangles.
        c. Count how many *non-overlapping* segments we can collect.
    3. If we find at least 3 such non-overlapping intervals along any axis, return True.

    ⏱️ Complexity Analysis:
    Time Complexity:
    - Sorting the rectangles takes O(n log n)
    - The loop runs in O(n)
    - Total: O(n log n) for each axis → O(n log n) overall

    Space Complexity:
    - O(1) extra space (in-place sort, constant tracking variables)
    """

    def can_cut(self, rectangles, axis):
        # Sort rectangles by the start of the current axis (x or y)
        rectangles.sort(key=lambda rect: rect[axis])
        
        non_overlapping_cuts = 0  # Counter for how many valid cuts we can make
        previous_end = -1         # Tracks the end of the previous rectangle in this axis
        
        for rectangle in rectangles:
            # Extract current rectangle's start and end along the selected axis
            start_coord = rectangle[axis]
            end_coord = rectangle[axis + 2]  # +2 gives the end point in that axis (x2 or y2)

            # If this rectangle starts after the previous one ends, it's non-overlapping
            if start_coord >= previous_end:
                non_overlapping_cuts += 1

            # Update the furthest endpoint we've seen so far
            previous_end = max(previous_end, end_coord)

            # If we already have 3 or more non-overlapping cuts, we're done
            if non_overlapping_cuts >= 3:
                return True

        # Less than 3 valid cuts found along this axis
        return False