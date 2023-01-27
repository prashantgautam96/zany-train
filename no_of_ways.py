import heapq

class Solution:
    def countPaths(self, n, roads):
        # Creating an adjacency list for the given graph.
        adj = [[] for i in range(n)]
        for road in roads:
            adj[road[0]].append((road[1], road[2]))
            adj[road[1]].append((road[0], road[2]))

        # Defining a priority queue (min heap).
        pq = []

        # Initializing the dist array and the ways array
        # along with their first indices.
        dist = [1e9 for i in range(n)]
        ways = [0 for i in range(n)]
        dist[0] = 0
        ways[0] = 1
        heapq.heappush(pq, (0, 0))

        # Define modulo value
        mod = (int)(1e9 + 7)

        # Iterate through the graph with the help of priority queue
        # just as we do in Dijkstra's Algorithm.
        while len(pq) > 0:
            dis, node = heapq.heappop(pq)

            for adjNode, edW in adj[node]:
                if dis + edW < dist[adjNode]:
                    dist[adjNode] = dis + edW
                    heapq.heappush(pq, (dis + edW, adjNode))
                    ways[adjNode] = ways[node]
                elif dis + edW == dist[adjNode]:
                    ways[adjNode] = (ways[adjNode] + ways[node]) % mod

        # Finally, we return the no. of ways to reach
        # (n-1)th node modulo 10^9+7.
        return ways[n - 1] % mod

# Driver Code.
n = 7

edges = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], 
[3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]

obj = Solution()

ans = obj.countPaths(n, edges)

print(ans)
