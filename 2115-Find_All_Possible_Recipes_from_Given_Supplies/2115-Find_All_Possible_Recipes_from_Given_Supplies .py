class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        Intuition:
        Solve the problem by treating it as determining which nodes (recipes) can be fully reached in a graph
        where nodes are recipes, and edges are ingredients needed to make these recipes.

        Approach:
        1. Construct a graph representation where each ingredient points to recipes that require it.
        2. Use a queue mechanism to process each available ingredient and subsequently recipes that can be made.
        3. Use in-degree tracking to determine when a recipe has all its necessary ingredients available.
        
        Complexity:
        Time: O(V + E) where V is the number of recipes and E is the number of total ingredient-recipe relations.
        Space: O(V + E) for storing the graph and the in-degree counts.

        :param recipes: List of strings representing the names of recipes.
        :param ingredients: List of lists, each sublist contains ingredients needed for the corresponding recipe.
        :param supplies: List of strings representing initially available ingredients.
        :return: List of recipes that can be created.
        """

        # Graph where keys are ingredients and values are lists of recipes that need that ingredient
        graph = {}
        # Dictionary to track the number of ingredients still needed for each recipe
        in_degree = {}

        # Build the graph and initialize in-degrees
        for recipe, req_ingredients in zip(recipes, ingredients):
            for ingredient in req_ingredients:
                if ingredient not in graph:
                    graph[ingredient] = []
                graph[ingredient].append(recipe)
                if recipe not in in_degree:
                    in_degree[recipe] = 0
                in_degree[recipe] += 1

        # Initialize the queue with the supplies available
        queue = supplies[:]
        # List to store the recipes that can be made
        result = []

        # Process the queue
        while queue:
            current_ingredient = queue.pop(0)

            # If this ingredient can help make any recipes
            if current_ingredient in graph:
                for recipe in graph[current_ingredient]:
                    in_degree[recipe] -= 1
                    # If all ingredients for this recipe are now available, add to the result and queue
                    if in_degree[recipe] == 0:
                        queue.append(recipe)
                        result.append(recipe)

        return result

# Continue to push the boundaries of what you can do! 🚀🔥
