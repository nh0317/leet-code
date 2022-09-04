from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def bfs(self, node):
        q= deque()
        q.append(node)
        visited = set([node.val])
        cnt = 0
        while q:
            u= q.popleft()
            cnt += 1
            for v in u.neighbors:
                if v.val not in visited:
                    q.append(v)
                    visited.add(v.val)
        return cnt 
    
    def clone_nodes(self, node, cnt):
        q= deque()
        q.append(node)
        nodes = [Node() for _ in range(cnt+1)]
        visited = set([node.val])
        while q:
            u= q.popleft()
            nodes[u.val] = Node(u.val, [])
            
            for v in u.neighbors:
                if v.val not in visited:
                    q.append(v)
                    visited.add(v.val)
        return nodes
    
    def clone_graph(self, node, nodes):
        root = Node()
        q= deque()
        q.append([node, root])
        visited = set()
        while q:
            u, r= q.popleft()
            r.val = u.val
            
            for i,v in enumerate(u.neighbors):
                r.neighbors.append(nodes[v.val])
                if v.val not in visited:
                    q.append([v,r.neighbors[i]])
                    visited.add(v.val)
        return root
        
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return 
        
        cnt = self.bfs(node)
        
        nodes= self.clone_nodes(node, cnt)
        root = self.clone_graph(node, nodes)
        
        return nodes[node.val]