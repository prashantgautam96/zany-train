import collections

class DisjointSet:
    def __init__(self, n):
        self.rank = [0]*(n+1)
        self.parent = list(range(n+1))
        self.size = [1]*(n+1)

    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

class Solution:
    def isValid(self, newr, newc, n):
        return newr >= 0 and newr < n and newc >= 0 and newc < n
    
    def MaxConnection(self, grid):
        n = len(grid)
        ds = DisjointSet(n * n)
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0: continue
                dr = [-1, 0, 1, 0]
                dc = [0, -1, 0, 1]
                for ind in range(4):
                    newr = row + dr[ind]
                    newc = col + dc[ind]
                    if self.isValid(newr, newc, n) and grid[newr][newc] == 1:
                        nodeNo = row * n + col
                        adjNodeNo = newr * n + newc
                        ds.unionBySize(nodeNo, adjNodeNo)
        mx = 0
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1: continue
                dr = [-1, 0, 1, 0]
                dc = [0, -1, 0, 1]
                components = set()
                for ind in range(4):
                    newr = row + dr[ind]
                    newc = col + dc[ind]
                    if self.isValid(newr, newc, n):
                        if grid[newr][newc] == 1:
                            components.add(ds.findUPar(newr * n + newc))
                sizeTotal = 0
                for it in components:
                    sizeTotal += ds.size[it]
                mx = max(mx, sizeTotal + 1)
        for cellNo in range(n * n):
            mx = max(mx, ds.size[ds.findUPar(cellNo)])
        return mx

s = Solution()
grid = [[1, 1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 0]]
print(s.MaxConnection(grid))
