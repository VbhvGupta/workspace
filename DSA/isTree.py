class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        if len(edges) != n-1 :
            return False

        m = collections.defaultdict(list)
        for el in edges :
            m[el[0]].append(el[1])
            m[el[1]].append(el[0])

        visited = []
        queue = [0]
        while queue:
            cur = queue.pop()
            visited.append(cur)
            queue += [node for node in m[cur] if node not in visited]

        return len(visited) == n
