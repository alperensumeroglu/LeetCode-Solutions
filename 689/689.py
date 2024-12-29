class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int, m=3) -> List[int]:
        # Space and Time O(n)
        window_sums = [sum(nums[:k])]
        for i in range(1, len(nums) - k + 1):
            window_sums.append(window_sums[-1] - nums[i - 1] + nums[i + k - 1])

        # Space O(m^2)
        max_sums = collections.defaultdict(lambda: [0, []])

        # Time O(m*n)
        for s in range(len(nums) - k * m + 1):  # O(n)
            for i in range(1, m + 1):  # O(m)
                l = s + (i - 1) * k
                window_sum = window_sums[l]
                if window_sum + max_sums[i - 1][0] > max_sums[i][0]:
                    max_sums[i][0] = window_sum + max_sums[i - 1][0]
                    max_sums[i][1] = max_sums[i - 1][1] + [l]
        
        return max_sums[m][1]
