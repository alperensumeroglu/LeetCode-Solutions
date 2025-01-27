class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # Create a list of tuples containing each number and its original index, then sort it by number
        indexed_nums = sorted([(nums[i], i) for i in range(len(nums))])
        
        # Initialize the resulting array
        result = [0] * len(nums)
        
        # Initialize pointers and a list to keep track of indices for swapping
        prev_num = indexed_nums[0][0]
        left_pointer = 0
        swap_indices = []
        
        for num, idx in indexed_nums:
            # If the difference between the current and previous number exceeds the limit
            if num - prev_num > limit:
                # Process the collected indices to finalize swaps within the limit range
                for index in sorted(swap_indices):
                    result[index] = indexed_nums[left_pointer][0]
                    left_pointer += 1
                swap_indices = []  # Reset swap indices for the next segment
            
            prev_num = num  # Update the previous number
            swap_indices.append(idx)
        
        # Finalize swaps for the remaining indices
        for index in sorted(swap_indices):
            result[index] = indexed_nums[left_pointer][0]
            left_pointer += 1
        
        return result
