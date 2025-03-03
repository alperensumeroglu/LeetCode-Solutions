class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        # Initialize lists to store elements based on their relation to the pivot
        smaller, equal, greater = [], [], []
        
        # Categorize elements into respective lists
        for num in nums:
            if num < pivot:
                smaller.append(num)  # Elements smaller than pivot
            elif num == pivot:
                equal.append(num)  # Elements equal to pivot
            else:
                greater.append(num)  # Elements greater than pivot

        # Concatenate lists to maintain the required order
        return smaller + equal + greater

'''

🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote

💡If this helped, don’t forget to upvote! 🚀🔥

**Intuition**  
The problem requires us to reorder an array while maintaining relative order among elements smaller than, equal to, and greater than a given pivot. The best approach is to classify elements into three categories and then merge them.

**Approach**  
We iterate through the array and divide the elements into three lists:  
- One for elements smaller than the pivot  
- One for elements equal to the pivot  
- One for elements greater than the pivot  

Finally, we concatenate these lists in the correct order and return the result.

**Complexity**  
• Time complexity: $$O(n)$$, since we iterate through the list once and use list concatenation, which is also $$O(n)$$.  
• Space complexity: $$O(n)$$, as we use three additional lists to store the categorized elements.

'''