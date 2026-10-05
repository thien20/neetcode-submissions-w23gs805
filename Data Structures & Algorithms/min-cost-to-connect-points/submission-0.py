class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_dist = [float("inf")] * n
        visited = set()
        ans = 0
        heap = []
        heapq.heappush(heap, [0,0]) # weight , node
        while heap:
            cost, node = heapq.heappop(heap)
            
            if node in visited:
                continue
            visited.add(node)
            x1, y1 = points[node]
            ans += cost
            for i in range(n):
                x2, y2 = points[i]
                new_cost = abs(x2-x1) + abs(y2-y1)

                if new_cost < min_dist[i]:
                    min_dist[i] = new_cost
                    heapq.heappush(heap, (new_cost, i))


        return ans

