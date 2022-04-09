class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        recipesMap = {}
        inDegrees = [0]*len(recipes)
        outgoing = defaultdict(set)
        result = []
        suppliesSet = set()
        for i in range(len(recipes)):
            recipesMap[recipes[i]] = i

        for i in supplies:
            suppliesSet.add(i)

        for i in range(len(ingredients)):
            for ingredient in ingredients[i]:
                if ingredient in recipesMap:
                    outgoing[recipesMap[ingredient]].add(i)
                    inDegrees[i] += 1

        queue = deque()

        for i in range(len(inDegrees)):
            if inDegrees[i] == 0:
                count = 0
                for ingredient in ingredients[i]:
                    if ingredient not in suppliesSet:
                        count += 1
                if count == 0:
                    queue.append(i)

        while queue:
            recipe = queue.popleft()
            print(outgoing)
            result.append(recipes[recipe])

            for neighbor in outgoing[recipe]:

                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    queue.append(neighbor)

        return result
