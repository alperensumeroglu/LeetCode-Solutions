from typing import List, Tuple

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[bool]:
        # Store the results
        results = [False] * len(queries)
        violating_positions = []  # Store the indices that violate the rule

        # Check the parity of consecutive elements
        for index in range(1, len(nums)):
            # If consecutive elements have the same parity, a violating index is found
            if nums[index] % 2 == nums[index - 1] % 2:
                violating_positions.append(index)

        # Check the results for each query
        for query_index in range(len(queries)):
            start = queries[query_index][0]
            end = queries[query_index][1]

            # Try to find a violating index in the given range
            has_violation = self.binarySearchForViolation(start + 1, end, violating_positions)

            # If there is no violation, the range is considered "special"
            results[query_index] = not has_violation

        return results

    def binarySearchForViolation(self, range_start: int, range_end: int, violating_positions: List[int]) -> bool:
        left = 0
        right = len(violating_positions) - 1

        # Check if a violating index exists in the range using binary search
        while left <= right:
            mid = left + (right - left) // 2
            violating_position = violating_positions[mid]

            if violating_position < range_start:
                left = mid + 1  # Check the right half
            elif violating_position > range_end:
                right = mid - 1  # Check the left half
            else:
                # If a violating index is found within the range, return true
                return True

        return False  # If no violating index is found in the range, return false
