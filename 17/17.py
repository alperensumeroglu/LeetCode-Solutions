class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If the input is empty, return an empty list
        if not digits:
            return []
        
        # Mapping of digits to corresponding letters (like on a phone keypad)
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # List to store all possible combinations
        combinations = []

        # Recursive function to generate combinations
        def helperFunction(index, currentString):
            # If all digits are processed, add the current string to the result
            if index == len(digits):
                combinations.append(currentString)
            else:
                # Iterate through the letters for the current digit
                for letter in phone[digits[index]]:
                    # Append the current letter and move to the next digit
                    helperFunction(index + 1, currentString + letter)

        # Start the recursive function with the first digit and an empty string
        helperFunction(0, "")

        # Return the list of all combinations
        return combinations
