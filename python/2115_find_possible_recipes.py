from collections import defaultdict
from typing import List


class Solution:

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        ing_to_recipe = defaultdict(list)
        in_degrees = {recipe: 0 for recipe in recipes}

        for recipe_idx in range(len(recipes)):
            recipe = recipes[recipe_idx]
            for ingredient in ingredients[recipe_idx]:
                if ingredient not in supplies:
                    ing_to_recipe[ingredient].append(recipe)
                    in_degrees[recipe] += 1

        completed_recipes = []
        queue = [k for k, v in in_degrees.items() if v == 0]

        while len(queue) > 0:
            recipe = queue.pop()
            completed_recipes.append(recipe)
            for target_recipe in ing_to_recipe[recipe]:
                in_degrees[target_recipe] -= 1
                if in_degrees[target_recipe] == 0:
                    queue.append(target_recipe)

        return completed_recipes


if __name__ == '__main__':
    s = Solution()
    inputs = [
        {'recipes': ["sandwich", "bread"],
         'ingredients': [["bread", "meat"], ["yeast", "flour"]],
         'supplies': ["yeast", "flour", "meat"]},
        {'recipes': ["bread", "sandwich", "burger"],
         'ingredients': [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
         'supplies': ["yeast", "flour", "meat"]}
    ]

    selected_input = 1
    print(s.findAllRecipes(inputs[selected_input]['recipes'],
                           inputs[selected_input]['ingredients'],
                           inputs[selected_input]['supplies']))
