"""
src  |  dest
0    :  [1, 2, 3]
1    :  [4]

-there needs to be n - 1 edges, so 5 - 1 = 4 edges to be true
I realized how the src connects to the dest nodes but it can't be the other way around
as it makes a loop, which is not a tree
and it will be mapping to a new dest node
is this a tree traversal? No because the class doesn't have class TreeNode and it's left, right, val funcs so I think I use adjacent list

"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if n - 1 != len(edges):
            return False

        # undirected
        adjList = {i:[] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        def dfs(node, parent, visited):
            if node in visited:
                return False
            visited.add(node)

            for nei in adjList[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node, visited):
                    return False

            return True

        return dfs(0, -1, set())
                    




