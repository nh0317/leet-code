import heapq
  
class Solution:     
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:

        n = len(patience)
        
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append([v,1])
            graph[v].append([u,1])
        
        distance = [float('inf') for _ in range(n)]
        distance[0] = 0
        
        pq = []
        heapq.heappush(pq, [0, 0])
        
        while pq:
            w, u = heapq.heappop(pq)
            
            for v, weight in graph[u]:
                if distance[v] > w + weight:
                    distance[v] = w + weight
                    heapq.heappush(pq, [distance[v], v])
        
        cnt = -1
        for i in range(1,n):
            time =  distance[i] * 2
     
            send =  distance[i] * 2 // patience[i]
            
            if  distance[i] * 2 % patience[i] > 0 : 
                send += 1
            # msg = [(send-j) * patience[i] for j in range(send)]
            counting = patience[i] * send + time - patience[i]
            cnt = max(cnt, counting)
            
        return cnt + 1
        
        
        