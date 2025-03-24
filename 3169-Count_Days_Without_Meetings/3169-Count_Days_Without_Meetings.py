class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        """
        ✅ Intuition:
        We need to count how many days are completely free of meetings within a given total duration.
        Since meetings may overlap, it's inefficient to mark every individual day — especially when the input size is large.
        Instead, we can merge overlapping meeting intervals and compute the total number of occupied days.
        Then, subtract this from the total to get the number of free days.

        ✅ Approach:
        1. Sort the list of meeting intervals by their starting day.
        2. Iterate through the sorted list and merge all overlapping intervals:
           - If the current interval overlaps with the previous one, extend the previous.
           - If not, finalize the previous interval and start a new one.
        3. After merging, compute the total number of days covered by meetings using the merged intervals.
        4. Subtract the total busy days from the total available days to get the final result.

        ✅ Complexity:
        - Time Complexity: O(N log N), where N is the number of meetings. Sorting dominates.
        - Space Complexity: O(N), for storing the merged list of intervals.
        This approach efficiently avoids marking each day and is optimal for large input sizes.

        🚀🔥 Keep pushing boundaries — Clean code is your superpower!
        """

        if not meetings:
            return days

        # Step 1: Sort meetings by start time
        meetings.sort()

        # Step 2: Merge overlapping intervals
        merged = []
        current_start, current_end = meetings[0]
        
        for start, end in meetings[1:]:
            if start <= current_end:
                # Overlapping: extend the current meeting
                current_end = max(current_end, end)
            else:
                # Non-overlapping: push current and move to next
                merged.append((current_start, current_end))
                current_start, current_end = start, end
        merged.append((current_start, current_end))  # Add the last interval

        # Step 3: Calculate total days occupied by meetings
        busy_days = 0
        for start, end in merged:
            busy_days += end - start + 1  # Inclusive

        # Step 4: Subtract busy from total
        return days - busy_days
