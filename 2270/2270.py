class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        valid_splits = 0
        array_length = len(nums)

        for index, value in enumerate(nums):
            left_sum += value
            total_sum -= value

            # Check conditions for a valid split
            if index + 1 != array_length and left_sum >= total_sum:
                valid_splits += 1

        return valid_splits
