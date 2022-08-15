from collections import deque

class Solution:
    def __init__(self):
        self.visited = []
        
    def bfs(self,start, graph):
        q = deque([start])
        self.visited[start] = True
        cnt = 0
        
        while q:
            u = q.popleft()
            cnt+= 1
            
            for v in graph[u]:
                if not self.visited[v]:
                    q.append(v)
                    self.visited[v] = True
        return cnt 
    
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        graph = [[] for _ in range(n)]
        self.visited = [False for _ in range(n)]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        nodes = []
        for i in range(n):
            if not self.visited[i]:
                node=self.bfs(i,graph)
                nodes.append(node)
                
                if node == n:
                    return 0
        
        result = n * (n-1) // 2
        for node in nodes:
            result -= node * (node -1) // 2
                
        return result