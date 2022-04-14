class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj_map = defaultdict(list)
        dep_count = defaultdict(int)
        
        for idx, recipe in enumerate(recipes):
            for ingredient in ingredients[idx]:
                adj_map[ingredient].append(recipe)
            dep_count[recipe] = len(ingredients[idx])
        
        possible = []
        
        queue = deque(supplies)
        while queue:
            item = queue.popleft()
            
            for recipe in adj_map[item]:
                dep_count[recipe] -= 1
                if dep_count[recipe] == 0:
                    possible.append(recipe)
                    queue.append(recipe)
        
        return possible
