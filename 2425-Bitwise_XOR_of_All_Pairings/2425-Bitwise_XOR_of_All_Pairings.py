class Solution:
    def xorAllNums(self, arr1: List[int], arr2: List[int]) -> int:
        # Calculate the effective number of repetitions for each array
        # If the length of one array is odd, all elements of the other array contribute to the result
        repetitions_arr1 = len(arr2) % 2
        repetitions_arr2 = len(arr1) % 2

        # Calculate the XOR for elements in both arrays based on their repetitions
        result = 0
        if repetitions_arr1:
            for num in arr1:
                result ^= num  # XOR elements of arr1 if arr2's length is odd
        if repetitions_arr2:
            for num in arr2:
                result ^= num  # XOR elements of arr2 if arr1's length is odd

        return result
