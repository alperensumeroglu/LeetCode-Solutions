class Solution:
    def constructSmallestNumber(self, pattern: str) -> str:
        """
        Constructs the lexicographically smallest number that follows the given DI pattern.

        :param pattern: A string consisting of 'I' (increasing) and 'D' (decreasing).
        :return: The smallest possible number as a string.
        """

        length = len(pattern)
        stack = []
        result = ""

        for index in range(length + 1):
            # Push numbers into the stack
            stack.append(index + 1)

            # If we reach the end or encounter 'I', pop all elements from stack
            if index == length or pattern[index] == "I":
                while stack:
                    result += str(stack.pop())

        return result


"""
Intuition
This problem can be solved using a **monotonic stack** approach. The key idea is that when we encounter an 'I', 
we finalize the numbers in the decreasing order. When we encounter a 'D', we store numbers in the stack to be 
reversed when an 'I' appears.

Approach
1. Use a **stack** to store numbers temporarily.
2. Iterate through the pattern, pushing numbers into the stack.
3. If we reach an 'I' or the end of the pattern, pop all elements from the stack to maintain the required order.
4. The **lexicographically smallest** number is constructed by ensuring minimal values are used first.
5. Return the final string.

Complexity
- Time complexity: **O(n)**  
  Each number is pushed and popped exactly once, making this a linear operation.
  
- Space complexity: **O(n)**  
  In the worst case (all 'D's), we store up to **n+1** elements in the stack before popping them.
"""
