class Solution:
    """
    Intuition:
    The problem simulates dominoes falling over time. Each domino can be pushed to the left ('L') or right ('R'),
    or remain upright ('.'). We need to determine the final state after all dominoes have fallen according to the rules.

    The key idea is to track the effect of each 'R' and 'L' and fill in the intermediate dominoes based on which side
    pushes stronger or if they balance out.

    Approach:
    - Convert the input string into a list for easier modification.
    - Traverse the list:
        - If we find a 'R', we record its index as the last seen 'R'.
        - If we find a 'L':
            - If a 'R' was seen before, balance the dominoes between this 'R' and 'L' by filling from both ends towards the center.
            - If no 'R' was seen, we fill all dots leftwards from the previous section with 'L'.
    - After traversal, if a trailing 'R' remains without a matching 'L', push all remaining dominoes to the right.
    - Finally, join the list into a string and return the result.

    Complexity:
    - Time Complexity: O(n), where n is the length of the dominoes string. We traverse the list once and each domino is updated at most once.
    - Space Complexity: O(n), because we convert the input string to a list for in-place modifications.
    """

    def pushDominoes(self, dominoes: str) -> str:
        domino_list = list(dominoes)  # Convert string to list for easier manipulation
        n = len(domino_list)
        last_right_index = -1  # Tracks the last seen 'R'
        last_left_index = 0    # Tracks the last seen 'L' (for edge cases)

        for current_index, domino in enumerate(domino_list):
            if domino == 'R':
                # Fill any dots between the last 'R' and current 'R' with 'R'
                if last_right_index != -1:
                    for fill_index in range(last_right_index + 1, current_index):
                        domino_list[fill_index] = 'R'
                last_right_index = current_index  # Update the last seen 'R'
            elif domino == 'L':
                if last_right_index != -1:
                    # Balance dominoes between last 'R' and current 'L'
                    left_ptr = last_right_index + 1
                    right_ptr = current_index - 1
                    while left_ptr < right_ptr:
                        domino_list[left_ptr] = 'R'
                        domino_list[right_ptr] = 'L'
                        left_ptr += 1
                        right_ptr -= 1
                    last_right_index = -1  # Reset because this 'L' stops the 'R' effect
                else:
                    # Fill all dots leftwards with 'L'
                    for fill_index in range(last_left_index, current_index):
                        if domino_list[fill_index] == '.':
                            domino_list[fill_index] = 'L'
                last_left_index = current_index  # Update the last seen 'L'

        # After traversing, if there's a pending 'R' at the end, fill the rest with 'R'
        if last_right_index != -1:
            for fill_index in range(last_right_index + 1, n):
                domino_list[fill_index] = 'R'

        return ''.join(domino_list)  # Convert list back to string and return

# 🚀🔥 Keep coding and stay awesome!
