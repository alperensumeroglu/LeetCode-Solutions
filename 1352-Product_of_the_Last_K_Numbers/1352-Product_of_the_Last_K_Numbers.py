class ProductOfNumbers:
    def __init__(self):
        # List to store prefix products
        self.prefix_products = []
        # Variable to maintain the running product
        self.running_product = 1

    def add(self, num: int) -> None:
        if num == 0:
            # If zero is added, reset prefix products
            self.prefix_products = []
            self.running_product = 1
        else:
            # Multiply running product and store it
            self.running_product *= num
            self.prefix_products.append(self.running_product)

    def getProduct(self, k: int) -> int:
        if len(self.prefix_products) < k:
            # If k is greater than available elements, return 0
            return 0
        elif k == len(self.prefix_products):
            # If k is equal to total elements, return the last prefix product
            return self.running_product
        else:
            # Otherwise, return the ratio of last k products
            return self.prefix_products[-1] // self.prefix_products[-1 - k]


'''
Intuition
This problem requires maintaining a stream of numbers and efficiently calculating the product of the last k numbers. 
Instead of storing all elements, we can use prefix products to get the product in constant time.

Approach
1. Maintain a list of prefix products.
2. When adding a number:
   - If it's zero, reset everything since multiplying by zero invalidates the previous prefix products.
   - Otherwise, multiply it with the last stored product and append it.
3. When querying for the product of the last k numbers:
   - If k is larger than available numbers, return 0.
   - If k is exactly the number of elements stored, return the last prefix product.
   - Otherwise, divide the last prefix product by the prefix product at index `-1 - k`.

Complexity
- Time complexity: O(1) for both `add` and `getProduct` operations.
- Space complexity: O(n), where n is the number of elements stored in prefix_products.
'''