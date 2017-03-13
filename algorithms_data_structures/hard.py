# You are given a set of tasks that you need to resolve, these tasks can have dependencies on other tasks
# (from the ones you are given), meaning that if task A has as dependency task B, then B needs to be resolved before A.
# Return a valid order in which you can resolve all your tasks. (Depth First Search)

class Task:
    def __init__(self, id):
        self.id = id
        self.dependecies = list()
        self.solved = False

    def resolve(self, externalResolve=None):
        """
        :param externalResolve: a function that can do something for any task
        """
        if not self.solved:
            for dep in self.dependecies:
                dep.resolve()
            if externalResolve:
                externalResolve(self)
            self.solved = True


def resolveTasks(tasks):
    valid_order_ids = list()
    def resolver(task):
        valid_order_ids.append(task.id)

    for t in tasks:
        t.resolve(resolver)

    return valid_order_ids



# count the number of islands in map (1=land, 0=water)
# 		1 1 0 0
# 		0 0 1 1   →  3 islands (cells not connected on diagonal)
#       1 0 0 1


def countIslands(map):
    if not map or not map[0]:
        raise Exception("Invalid map!")

    visited = 2
    land = 1

    def valid_land(i, j):
        return i >= 0 and j >= 0 and i < len(map) and j < len(map[0])

    def visit_land(i, j):
        """
        DFS or seed fill algorithm on up,down,left,right neighbors
        """

        if map[i][j] == land:
            for x, y in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
                if valid_land(i, j):
                    visit_land(x, y)

            map[i][j] = visited



    n_islands = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == land:
                visit_land(i, j)
                n_islands += 1

    return n_islands



# Given an array of coin values and a target sum of money return the number of ways in which you can represent that sum
# of money with the given coin values. (More complicated recursion / dynamic programming)

def getChangeRecursive(coins, sum):
    n_ways = 0
    for c in coins:
        n_ways += getChangeRecursive(coins, sum - c)

    return n_ways

def getChangeDynamic(coins, sum):
    dp = [0]*(sum+1)
    for c in coins:
        if c <= sum:
            dp[c] = 1

    for i in range(sum+1):
        for c in coins:
            if c <= i:
                dp[i] += dp[i-c]
    return dp[-1]






