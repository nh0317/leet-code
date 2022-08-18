import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        pq = []
        
        dp = [[float('inf') for _ in range(len(heights[0]))] for _ in range(len(heights))]
        heapq.heappush(pq, [0,0,0])
        
        while pq:
            effort , y, x = heapq.heappop(pq)
            
            for dy, dx in [[1,0],[-1,0],[0,1],[0,-1]]:
                ny, nx = y + dy, x + dx
                
                if 0<=ny<len(heights) and 0 <= nx < len(heights[0]):
                    e = max(effort, abs(heights[ny][nx] - heights[y][x]))
                    
                    if e < dp[ny][nx]:
                        dp[ny][nx] = e
                        heapq.heappush(pq, [e,ny,nx])
                        
        return dp[-1][-1] if dp[-1][-1] != float('inf') else 0